def get_base_knowledge(key=""):
    knowledge = """
    BRSET Dataset Overview
Introduction
The BRSET (Brazilian Multilabel Ophthalmological Dataset) was developed by researchers from São Paulo Federal University and Massachusetts Institute of Technology to advance machine learning research in ophthalmology. BRSET represents the first publicly available Brazilian multilabel ophthalmological dataset, offering a comprehensive resource for developing AI models to predict demographic characteristics and multi-label disease classification using retinal fundus photos. The dataset addresses the critical need for representative data from low and middle-income countries to reduce bias in ophthalmological AI systems.

Data Collection
Collection Sites: Data was acquired from three Brazilian ophthalmological centers in São Paulo with a total of 16,266 images from 8,524 patients evaluated from 2010 to 2020.
Devices Used:
o10,591(65.11%) images were captured using Nikon NF505 (Tokyo, Japan), and 5,675(34.89%) images were captured using Canon CR-2 (Canon Inc., Melville, NY) retinal camera.
oIn all images, the viewpoint is macula centered.
Patient Diversity:
o8,524 patients from diverse Brazilian backgrounds.
oGender distribution: 6,214(38.20%) male, 10,052(61.80%) female patients.
oAverage age: 57.84 years (SD 18.27).
oAge range: 5-97 years.
Each patient has one image for left and right eyes respectively. Following two images is from the same patient with id=33.

Download and Use Policy
The dataset is freely available for non-commercial use.
Access requires completion of CITI Data or Specimens Only Research training.
Researchers must sign a data use agreement via PhysioNet.
Access is restricted to credentialed users who sign the Data Use Agreement (DUA). Dataset download website: BRSET Download Page.

Dataset Content
Attribute	Details
Image Count	16,266 color fundus images from 8,524 patients
Resolution	Variable (exported directly from cameras in JPEG format, e,g. 951×874 pixels, 2,984×2,304 pixels ,etc.)
Modality	Fundus photography (retinal cameras)
Labels	Multi-label classification system covering:
Anatomical Classification: the retinal optic disc, retinal vessel, and macula aspects were classified as normal or abnormal.
Quality Control Parameters: the image focus, illumination, image field, and artifacts were classified as satisfactory or unsatisfactory.
Pathological Classifications: diabetic retinopathy, diabetic macular edema, scar (toxoplasmosis), nevus, age-related macular degeneration(amd), vascular occlusion, hypertensive retinopathy, drusens, nondiabetic retinal hemorrhage, retinal detachment, myopic fundus, increased cup disc ratio, other.
Structure	Fundus photos with comprehensive metadata file containing patient demographics and clinical characteristics.
Multiview	Each image is macula-centered; paired left and right eye images available for same patient.

Labeling and Dataset Statistics for BRSET
Anatomical Classification
Multiple binary classifications (1 normal, 2 abnormal).
Anatomical parameters	normal	abnormal
Optic Disc	12,986(79.83%)	3,279(20.16%)
Vessels	15,459(95.04%)	807(4.96%)
Macula	11,589(71.25%)	4,677(28.75%)

Diabetic Retinopathy Classification
BRSET provides comprehensive ICDR-based (0-4) and SDRG-based (0-4) grading.
Grading Type	Subtype	Percentage
International Clinic Diabetic Retinopathy （ICDR） classification	No retinopathy(0)	15,183(93.34%)
	Mild non-proliferative diabetic retinopathy(1)	158(0.97%)
	Moderate non-proliferative diabetic retinopathy(2)	451(2.77%)
	Severe non-proliferative diabetic retinopathy(3)	78(0.48%)
	Proliferative diabetic retinopathy and post-laser status(4)	396(2.43%)
Scottish Diabetic Retinopathy Grading (SDRG) classification 	No retinopathy(0)	15,188(93.37%)
	Mild Background(1)	280(1.72%)
	Moderate Background(2)	133(0.82%)
	Severe non-proliferative or pre-proliferative diabetic retinopathy(3)	263(1.62%)
	Proliferative diabetic retinopathy and post-laser status(4)	402(2.47%)
The statistical results of the consistency of DR grading by ICDR (left and right eyes) are as follows:
Patients level	Total patient	8,524
	Patient with only one image	804(9.43%)
Patients Eye level	Multiple images of a patient with only one eye	108(1.27%)
	Patients with images of both eyes	7,612(89.30%)
Label level 	Multiple images with only one eye	Consistent DR grades	106(1.24%)
		Inconsistent DR grades	2(0.02%)
	Only one image for both eyes	Consistent DR grading in both eyes	7,401(86.83%)
		Inconsistent DR grading in both eyes	198(2.32%)
	Multiple images for the left eye, one image for the right eye	Consistent DR grading in both eyes	5(0.06%)
		Inconsistent DR grading in both eyes	0
	Multiple images for the right eye, one image for the left eye	Consistent DR grading in both eyes	1(0.01%)
		Inconsistent DR grading in both eyes	0
	Multiple images for the left eye, Multiple images for the right eye	Consistent DR grading in both eyes	6(0.07%)
		Inconsistent DR grading in both eyes	1(0.01%)

Eye Disease Classification
Multiple binary classifications (1 present, 0 absent).

Classification parameters	present	absent
Diabetic retinopathy	1,070(6.58%)	15,196(93.42%)
Macular edema	401(2.47%)	15,865(97.53%)
Scar	291(1.79%)	15,975(98.21%)
Nevus	130(0.80%)	16,136(99.20%)
Age-related macular degeneration	299(1.84%)	15,967(98.16%)
Vascular occlusion	101(0.62%)	16,165(99.38%)
Hypertensive retinopathy	284(1.75%)	15,982(98.25%)
Drusens	2,833(17.42%)	13,433(82.58%).
Hemorrhage	95(0.58%)	16,171(99.42%)
Retinal detachment	7(0.04%)	16,259(99.96%)
Myopic fundus	270(1.66%)	15,996(98.34%)
Increased cup-disc ratio	3,205(19.71%)	13,061(80.29%)
Other	820(5.05%)	15,446(94.95%)

*Differences Diabetic retinopathy statistics and DR Grading (ICDR-based and SDRG-based)

Image Quality Assessment 
(probably manual annotation)
A retinal specialist ophthalmologist quality-assessed all the images based on the following criteria, and the quality assessment was as follows (1 normal, 2 abnormal).
Illumination	This parameter is graded as adequate when both of the following requirements are met: 1) Absence of dark, bright, or washed-out areas that interfere with detailed grading; 2) In the case of peripheral shadows (e.g., due to pupillary constriction) the readable part should reach more than 80% of the whole image.	16,182(99.48%) Normal, 84(0.52%) Abnormal
Image Field	This parameter is graded as adequate when all the following requirements are met: 1) The optic disc is at least 1 disc diameter (DD) from the nasal edge; 2) The macular center is at least 2 DD from the temporal edge; 3) The superior and inferior temporal arcades are visible in a length of at least 2 DD	14,865(91.39%) Normal, 1,401(8.61%) Abnormal
Artifacts	The following artifacts are considered: haze, dust, and dirt. This parameter is graded as adequate when the image is sufficiently artifact-free to allow adequate grading.	16,209(99.65%) Normal, 57(0.35%) Abnormal
Focus	This parameter is graded as adequate when the focus is sufficient to identify third-generation branches within one optic disc diameter around the macula.	15,723(96.66%) Normal, 541(3.33%) Abnormal



Performance Evaluation on RETFound
Freeze:  Linear_Probe (Freeze Encoder) and linear head.
FT:  Fine tune (update encoder and linear head).
Internal_Test:  BRSET Test dataset
External_Test:  mBRSET ALL data
Label:  Diabetic Retinopathy (DR) Classification & Macular Edema (MDE) Classification.
Data Split:  55:15:30 Random, Shuffle in Train, Val, Test Reference Paper (2023, nature).
Training Setting: model(RETFound_mae), epoch(100), batch size(128), input size(224),  learning rate(5e-3), random seed(0).
Experimental equipment: GeForce RTX 5090
Performance of DR Classification by the RETFound_mae_natureCFP model.
Fig.1 experimental results reveal that the frozen RETFound model achieves only 91.73% AUC without fine-tuning, while fine-tuning can greatly improve performance, with AUC reaching 96.00% on the internal BRSET test dataset and accuracy reaching 96.19%. However, external evaluation on mBRSET shows notable decline with AUC dropping to 79.74% and accuracy to 79.46%, indicating limited cross-domain generalization capability despite the model's strong performance on internal validation, highlighting the challenges of deploying foundation models across diverse clinical datasets.

Fig. 1 Comparsion of the performance of the RETFound model DR Classification in BRSET (Internal test) and mBRSET(External test)

We use the Transformer Attribution (2021, CVPR) method for visualization experiments. Fig.2 demonstrates CAM visualizations across diabetic retinopathy severity levels on the BRSET dataset. DR_ICDR 0 shows minimal activation indicating no pathological features, while progressive severity (DR_ICDR 1-2) exhibits increasing attention on optic disc and macular regions consistent with early microvascular changes. DR_ICDR 3 displays concentrated activation on hard exudates and hemorrhages, and DR_ICDR 4 shows focal attention on neovascularization sites. These results confirm the model's ability to identify clinically relevant pathological features across different severity grades on the BRSET dataset.

Fig. 2 CAM Visualizations of RETFound_mae_natureCFP-FT Model for Different Grades of Diabetic Retinopathy

Performance of ME Classification by the RETFound_mae_natureCFP model.
Fig.3 demonstrates the critical importance of fine-tuning for downstream diabetic macular edema classification, as evidenced by the substantial performance gap between the frozen RETFound_mae_natureCFP model (green bars) and the fine-tuned version (brown and red bars). Accuracy improves dramatically from 97.91% to 98.95% and AUC increases from 94.58% to 98.72% after fine-tuning on internal validation. However, external evaluation reveals significant performance degradation, with accuracy dropping to 94.55% and AUC declining to 93.12%, indicating limited cross-domain generalization capability. This finding suggests that while fine-tuning is essential for task-specific optimization, the model exhibits poor external adaptability across different datasets.


Fig. 3 Comparsion of the performance of the RETFound model MDE Classification in BRSET(Internal test) and mBRSET(External test)

We use the Transformer Attribution (2021, CVPR) method for visualization experiments. Fig.4 demonstrates distinct CAM activation patterns for diabetic macular edema classification on the BRSET dataset. Non-Edema cases exhibit diffuse activation across multiple retinal regions, while Edema cases show highly localized activation concentrated in specific macular areas where fluid accumulation occurs. This indicates that the model successfully identifies and localizes pathological edematous regions, demonstrating accurate lesion detection capability.

Fig. 4 CAM Visualizations of RETFound_mae_natureCFP-FT Model for MDE Classification on BRSET Dataset

    
    mBRSET Dataset Overview
Introduction
The mBRSET (Mobile Brazilian Retinal Dataset) was developed by researchers from Sao Paulo Federal University and Massachusetts Institute of Technology, to support research in portable diabetic retinopathy (DR) screening. mBRSET dataset represents the first publicly available collection of retinal images captured via handheld retinal cameras in real-life, high-burden scenarios, offering a comprehensive resource for addressing the challenges of diabetic retinopathy screening and management in underserved populations.

Data Collection
Collection Sites: Data was acquired during the Itabuna Diabetes Campaign in November 2022 in Itabuna, Bahia State, Northeast Brazil. Collection took place in a real-world, community-based screening environment representing typical low and middle-income country settings.
Devices Used:
oImages were captured using a Phelcom Eyer (Phelcom Technologies, Sao Carlos, Brazil) portable, handheld, smartphone-based retinal fundus camera.
oThe Eyer camera captures retinal images at a 45° angle, the image viewpoint can be macula-centered or optic disc-centered.
Patient Diversity:
o1291 patients from diverse ethnic backgrounds.
oGender distribution: 3,360(65.07%) female, 1,804(34.93%) male patients.
oAverage age: 61.44 years (SD 11.63).
oDiabetes duration: Average 9.53 years (SD 8.64)
oOral treatment: 1,083 patients (84.61%)
oInsulin therapy: 266 patients (20.79%)
oSystemic hypertension: 914 patients (71.4%)
oAlcohol consumption: 178 patients (14.0%)
oSmoking: 81 patients (6.4%)
oObesity: 102 patients (8.0%)
oVascular disease: 217 patients (17.1%)
oAcute myocardial infarction: 98 patients (7.7%)
oNephropathy: 46 patients (3.6%)
oNeuropathy: 55 patients (4.3%)
oDiabetic foot: 173 patients (13.7%)
oNearly half of the population has European ancestry, around 40% trace back to African ancestry, and 10% carry Native American ancestry.
Each Patient has two images for left and right eyes respectively. Following four images is from the same patient with id=1006 (1006.1 and 1006.2 are right eyes while 1006.3 and 1006.4 are left eye ).  Left and right eyes may have different diseases (e.g., DR grading) diagnosis.


Download and Use Policy
The dataset is freely available for non-commercial use.
Access requires completion of CITI Data or Specimens Only Research training.
Researchers must sign a data use agreement via PhysioNet.
Access is restricted to credentialed users who sign the Data Use Agreement (DUA). Dataset download website: mBRSET Download Page.

Dataset Content
Attribute	Details
Image Count	5,164 color fundus images from 1,291 patients
Resolution	1,600×1,600 pixels
Modality	Fundus photography (smartphone-based portable camera)
Labels	The label consists of two parts:
Quality control parameters: The evaluation of parameters encompasses the detection of artifacts, which encompass various issues such as image focus, illumination discrepancies, and the presence of dust.
Diabetic retinopathy classification: Diabetic retinopathy and diabetic macular edema were classified using the International Clinic Diabetic Retinopathy (ICDR) grading.
Structure	Patient display screen photographs and structured metadata file containing patient demographic information and clinical characteristics
Multiview	Each image is macula-centered or optic disc-centered; paired left and right eye images available for same patient

Labeling and Dataset Statistics for mBRSET
Diabetic Retinopathy Classification
mBRSET provides comprehensive ICDR-based (0-4) grading. The labeled data in the dataset is 4884 images.
Grading Type	Subtype	Percentage
International Clinic Diabetic Retinopathy （ICDR） classification	No retinopathy(0)	3,750(76.78%)
	Mild non-proliferative diabetic retinopathy(1)	272(5.57%)
	Moderate non-proliferative diabetic retinopathy(2)	568(11.63%)
	Severe non-proliferative diabetic retinopathy(3)	82(1.68%)
	Proliferative diabetic retinopathy and post-laser status(4)	212(4.34%)
The statistical results of the consistency of DR grading by ICDR (left and right eyes) are as follows:
Patients level	Total patient	1,291
Patients Eye level	Patients with images of both eyes	1,291(100.00%)
Label level	Only consider multiple left-eye images	Consistent DR grades	1,099(85.13%)
		Inconsistent DR grades	192(14.87%)
	Only consider multiple right-eye images	Consistent DR grades	1,077(83.42%)
		Inconsistent DR grades	214(16.58%)
	Consider both eyes	Inconsistent DR grading across multiple images in both eyes	54(4.18%)
		Inconsistent DR grading in left eye across multiple images	138(10.69%)
		Inconsistent DR grading in right eye across multiple images	160(12.39%)
		Consistent DR grading in both eyes	856(66.31%)
		Inconsistent DR grading in both eyes	83(6.43%)

Diabetic Macular Edema Classification
Binary classification for Diabetic Macular Edema (yes or no). The labeled data in the dataset is 4899 images.
Classification parameters	Yes	No
Macular edema	427(8.72%)	4472(91.28%)

Quality Assessment (Probably Manual annotation)
Two ophthalmologists, experts in retina and vitreous, meticulously labeled all the images according to predefined criteria set by the research group. The evaluation of parameters encompasses the detection of artifacts, which encompass various issues such as image focus, illumination discrepancies, and the presence of dust. Additionally, each image is categorized based on its quality, thus determining whether it is deemed satisfactory or unsatisfactory for clinical assessment. The labeled data in the dataset are 5164 images.
Quality control parameters	Yes	No
Artifacts	4272(82.73%)	892(17.27%)
Quality	4872(94.35%)	292(5.65%)

Performance evaluation on RETFound
Freeze:  Linear_Probe (Freeze Encoder) and linear head.
FT:  Fine tune (update encoder and linear head).
Internal_Test:  mBRSET Test dataset
External_Test:  BRSET ALL data
Label:  Diabetic Retinopathy (DR) Classification & Macular Edema (MDE) Classification.
Data Split:  55:15:30 Random, Shuffle in Train, Val, Test Reference Paper (2023, nature).
Training Setting: model(RETFound_mae), epoch(100), batch size(128), input size(224),  learning rate(5e-3), random seed(0).
Experimental equipment: GeForce RTX 5090
Performance of DR Classification by the RETFound_mae_natureCFP model.
Fig.1 experimental results reveal that the Freeze RETFound model achieves 81.00% AUC without fine-tuning, and fine-tuning can significantly improve performance, with AUC reaching 87.21% on the internal test dataset. However, external evaluation shows a decline to 85.30% AUC, indicating limited cross-domain generalization despite the relatively modest performance drop.


Fig. 1 Comparison of the performance of the RETFound model DR Classification in mBRSET (Internal test) and BRSET(External test)

We use the Transformer Attribution (2021, CVPR) method for visualization experiments. The CAM visualizations reveal distinct attention patterns corresponding to diabetic retinopathy severity levels (Fig.2). For DR_ICDR 0, the model shows minimal activation, indicating absence of pathological features. Progressive severity (DR_ICDR 1-2) demonstrates increasing focus on optic disc and macular regions, consistent with early microvascular changes. DR_ICDR 3 exhibits concentrated activation on hard exudates and hemorrhages, while DR_ICDR 4 shows focal attention on neovascularization sites. These results demonstrate that the model successfully learns clinically relevant pathological features, providing interpretable evidence for automated diabetic retinopathy diagnosis.

Fig. 2 CAM Visualizations of RETFound_mae_natureCFP-FT Model for Different Grades of Diabetic Retinopathy

Performance of MDE Classification by the RETFound_mae_natureCFP model.
Fig. 3 demonstrates the critical importance of fine-tuning for downstream task performance, as evidenced by the substantial performance gap between the frozen RETFound_mae_natureCFP model (green bars) and the fine-tuned version (brown and red bars) across all evaluation metrics, with accuracy improving from 92.45% to 95.58% on internal validation. The superior performance of the external test dataset (red bars) compared to the internal test (brown bars), with higher accuracy (97.53% vs 95.58%) and AUC (96.26% vs 94.64%), can be attributed to significant differences in image quality between the datasets. Specifically, the mBRSET(internal test) dataset contains 4,283 images (82.7%) with various imaging artifacts, which adversely affect model performance, while the external dataset exhibits better image quality. This finding suggests that while fine-tuning is essential for task-specific optimization, the model's sensitivity to artifact presence indicates limited robustness to degraded imaging conditions, highlighting potential challenges in clinical deployment where image quality variations are common.


Fig. 3 Comparison of the performance of the RETFound model MDE Classification in mBRSET(Internal test) and BRSET(External test)


We use the Transformer Attribution (2021, CVPR) method for visualization experiments. Fig.4 demonstrates distinct CAM activation patterns for diabetic macular edema classification on the BRSET dataset. Non-Edema cases exhibit diffuse activation across multiple retinal regions, while Edema cases show highly localized activation concentrated in specific macular areas where fluid accumulation occurs. This contrast indicates that the model successfully differentiates between normal retinal anatomy and pathological oedematous changes, accurately localizing disease-relevant regions.

Fig. 4 CAM Visualizations of RETFound_mae_natureCFP-FT Model for MDE Classification on mBRSET Dataset
    """

    return knowledge
