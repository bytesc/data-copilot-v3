import logging

import pandas as pd

from .tools.base_knowledge.get_base_knowledge import get_base_knowledge
from .tools.copilot.utils.code_insert import insert_lines_into_function
from .tools.tools_def import engine, llm, query_database, exe_sql

from .tools.copilot.python_code import get_py_code
from .tools.copilot.utils.code_executor import execute_py_code
from .tools.copilot.sql_code import get_db_info_prompt

from .tools.get_function_info import get_function_info

from .utils.final_output_parse import df_to_markdown, wrap_html_url_with_html_a, \
    wrap_csv_url_with_html_a
from .utils.final_output_parse import wrap_png_url_with_markdown_image, is_png_url, is_iframe_tag
from .utils.pd_to_csv import pd_to_csv
from .utils.pd_to_walker import pd_to_walker

IMPORTANT_MODULE = ["import math"]
THIRD_MODULE = ["import pandas as pd", "import numpy as np"]


def get_cot_code_prompt(question, tables=None, use_all_functions=False):
    rag_ans = ""
    knowledge = ""
    rag_ans = get_base_knowledge()
    knowledge = "\nBase knowledge: \n" + rag_ans + "\n"
    # print(rag_ans)

    function_set, function_info, function_import = get_function_info(question, llm, use_all_functions)
    # print(function_info)
    if function_info == "solved":
        return "solved", rag_ans, []
    print(function_info)

    database = ""
    if query_database in function_set or exe_sql in function_set:
        data_prompt = get_db_info_prompt(engine, tables=tables, simple=False, example=False)
        database = "\nThe database content: \n" + data_prompt + "\n"

    pre_prompt = """ 
Please use the following functions to solve the problem.
Please yield explanation string of each step as kind of report!
Please yield some information string during the function!
Please yield the result of each step and function call!
Please yield report many times during the function!!! not only yield at last! 
Please yield the tables used before query database function!!!
None or empty DataFrame return handling for each function call is extremely important.
If the user just ask to introduce or explain something, just yield the answer text in code without function call.
"""
    function_prompt = """ 
Here is the functions you can import and use:
"""
    module_prompt = "You can only use the third party function in " + str(THIRD_MODULE) + " !!!"

    #     example_code = """
    # Here is an example:
    # ```python
    # def func():
    #     import pandas as pd
    #     import math
    #     # generate code to perform operations here
    #
    #     original_question = "show me the grades of a A01 class?"
    #
    #     yield "A01 class’s grades are as follows:"  # yield some information and explanation
    #     yield "use table: stu_info ,stu_grade"  # yield tables names before query database function
    #     df = query_database("The grades of a A01 class, use table stu_info ,stu_grade", "Name, Course_name, Grade")
    #     yield df  # the result of each step and function call
    #     # None or empty DataFrame return handling for each function call.
    #     if df == None:
    #         yield "The grades for this class were not found in the database"
    #     else:
    #         data_description = explain_data("Analysis A01 class’s grades", df)
    #         yield data_description
    #         yield "The grade histogram is as follows:"
    #         path = draw_graph("Draw a bar chart", df)
    #         yield path
    # ```
    # """

    example_code = """
    Here is an example: 
    ```python
    def func():
        import pandas as pd
        import math
        # generate code to perform operations from here
        
        yield "A01 class’s grades are as follows:"  # yield some information and explanation
        yield "use table: stu_info ,stu_grade"  # yield tables names before query database function
        df = exe_sql(\"\"\"
            SELECT s.student_id, s.name, g.course, g.score FROM stu_info s
            JOIN stu_grade g ON s.student_id = g.student_id
            WHERE s.class = 'A01'
        \"\"\")   
        yield df # the result of each step and function call
        # None or empty DataFrame return handling for each function call.
        if df == None:
            yield "The grades for this class were not found in the database"
        else:
            data_description = explain_data("Analysis A01 class’s grades", df)
            yield data_description
            yield "The grade histogram is as follows:"
            path = draw_graph("Draw a bar chart", df) # use different type of chart based on the situation
            yield path
    ```
    """
    cot_prompt = "question:" + question + knowledge + database + pre_prompt + \
                 function_prompt + str(function_info) + \
                 module_prompt + example_code
    return cot_prompt, rag_ans, function_import


def cot_agent(question, tables=None, use_all_functions=False, retries=2, print_rows=10):
    exp = None
    for i in range(retries):
        cot_prompt, rag_ans, function_import = get_cot_code_prompt(question, tables, use_all_functions)
        print(rag_ans)
        # print(cot_prompt)
        if cot_prompt == "solved":
            return rag_ans, ""
        else:
            err_msg = ""
            for j in range(retries):
                code = get_py_code(cot_prompt + err_msg, llm)
                # print(code)
                # code = insert_yield_statements(code)
                code = insert_lines_into_function(code, function_import)
                code = insert_lines_into_function(code, IMPORTANT_MODULE)
                code = insert_lines_into_function(code, THIRD_MODULE)
                print(code)
                if code is None:
                    continue
                try:
                    result = execute_py_code(code)
                    cot_ans = ""
                    for item in result:
                        # print(item)
                        if isinstance(item, pd.DataFrame):
                            if item.index.size > 10:
                                cot_ans += df_to_markdown(item.head(print_rows)) + \
                                           "\nfirst {} rows of {}".format(print_rows, len(item)) + \
                                           "\nthe data above are just slice example, download csv to get full data\n"
                            else:
                                cot_ans += df_to_markdown(item)
                            html_link = pd_to_walker(item)
                            csv_link = pd_to_csv(item)
                            # cot_ans += wrap_html_url_with_markdown_link(html_link)
                            cot_ans += wrap_html_url_with_html_a(html_link)
                            cot_ans += wrap_csv_url_with_html_a(csv_link)
                        elif isinstance(item, str) and is_png_url(item):
                            cot_ans += "\n" + wrap_png_url_with_markdown_image(item) + "\n"
                        elif is_iframe_tag(str(item)):
                            cot_ans += "\n" + str(item) + "\n"
                        else:
                            cot_ans += "\n" + str(item) + "\n"
                        print(item)

                    ans = ""
                    # if rag_ans and rag_ans != "":
                    #     ans += "### Base knowledge: \n" + rag_ans + "\n\n"
                    ans += "### Result: \n" + cot_ans + "\n"
                    # print(ans)
                    # review_ans = get_ans_review(question, ans, code)
                    # ans += "## Summarize and review: \n" + review_ans + "\n"

                    logging.info(f"Question: {question}\nAnswer: {ans}\nCode: {code}\n")

                    return ans, code
                except Exception as e:
                    err_msg = "\n" + str(e) + "\n```python\n" + code + "\n```\n"
                    exp = e
                    print(e)
                    continue
    return None, None


def exe_cot_code(code, retries=2, print_rows=10):
    for j in range(retries):
        if code is None:
            continue
        cot_ans = ""
        try:
            result = execute_py_code(code)
            for item in result:
                if item is None:
                    item = " "
                print(item)
                if isinstance(item, pd.DataFrame):
                    if item.index.size > 10:
                        cot_ans += df_to_markdown(item.head(print_rows)) + \
                                   "\nfirst {} rows of {}".format(print_rows, len(item)) + \
                                   "\nthe data above are just slice example, download csv to get full data\n"
                    else:
                        cot_ans += df_to_markdown(item)
                    html_link = pd_to_walker(item)
                    csv_link = pd_to_csv(item)
                    # cot_ans += wrap_html_url_with_markdown_link(html_link)
                    cot_ans += wrap_html_url_with_html_a(html_link)
                    cot_ans += wrap_csv_url_with_html_a(csv_link)
                elif isinstance(item, str) and is_png_url(item):
                    cot_ans += "\n" + wrap_png_url_with_markdown_image(item) + "\n"
                elif isinstance(item, str) and is_iframe_tag(item):
                    html_map = str(item)
                    cot_ans += "\n" + html_map + "\n"
                else:
                    cot_ans += "\n" + str(item) + "\n"

        except Exception as e:
            print("Error:", e)
            if j < retries:
                continue
        # ans = "### Base knowledge: \n" + rag_ans + "\n\n"
        ans = "### Result: \n" + cot_ans + "\n"
        # print(ans)
        return ans
    return None


def get_cot_code(question, retries=2):
    cot_prompt, rag_ans, function_import = get_cot_code_prompt(question)
    print(rag_ans)
    # print(cot_prompt)
    if cot_prompt == "solved":
        return rag_ans, None
    else:
        err_msg = ""
        for j in range(retries):
            code = get_py_code(cot_prompt + err_msg, llm)
            # print(code)
            # code = insert_yield_statements(code)
            code = insert_lines_into_function(code, function_import)
            code = insert_lines_into_function(code, IMPORTANT_MODULE)
            code = insert_lines_into_function(code, THIRD_MODULE)
            print(code)
            if code is None:
                continue
            return code
