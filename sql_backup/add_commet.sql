-- Add table and column comments for brest table
ALTER TABLE `brest`
    COMMENT 'BRSET (Brazilian Multilabel Ophthalmological Dataset) - Contains retinal fundus images and comprehensive clinical metadata from Brazilian patients.';

ALTER TABLE `brest`
    MODIFY COLUMN `image_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Unique identifier for each fundus image',
    MODIFY COLUMN `patient_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Unique identifier for each patient',
    MODIFY COLUMN `camera` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Retinal camera model used: Nikon NF505 or Canon CR-2',
    MODIFY COLUMN `patient_age` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Age of the patient in years',
    MODIFY COLUMN `comorbidities` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Other medical conditions present',
    MODIFY COLUMN `diabetes_time_y` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Duration of diabetes in years',
    MODIFY COLUMN `insuline` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Whether patient uses insulin therapy (Yes/No)',
    MODIFY COLUMN `patient_sex` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Gender of patient (Male/Female)',
    MODIFY COLUMN `exam_eye` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Which eye was examined (Left/Right)',
    MODIFY COLUMN `diabetes` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Diabetes diagnosis (Yes/No)',
    MODIFY COLUMN `nationality` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Patient nationality or ethnic background',
    MODIFY COLUMN `optic_disc` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Optic disc classification: 1=normal, 2=abnormal',
    MODIFY COLUMN `vessels` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Retinal vessels classification: 1=normal, 2=abnormal',
    MODIFY COLUMN `macula` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Macula classification: 1=normal, 2=abnormal',
    MODIFY COLUMN `DR_SDRG` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Scottish Diabetic Retinopathy Grading: 0-4',
    MODIFY COLUMN `DR_ICDR` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'International Clinic Diabetic Retinopathy classification: 0-4',
    MODIFY COLUMN `focus` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Image focus quality: 1=adequate, 2=inadequate',
    MODIFY COLUMN `Illuminaton` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Image illumination quality: 1=adequate, 2=inadequate',
    MODIFY COLUMN `image_field` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Image field adequacy: 1=adequate, 2=inadequate',
    MODIFY COLUMN `artifacts` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Presence of artifacts: 1=adequate, 2=inadequate',
    MODIFY COLUMN `diabetic_retinopathy` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Diabetic retinopathy presence: 1=present, 0=absent',
    MODIFY COLUMN `macular_edema` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Diabetic macular edema presence: 1=present, 0=absent',
    MODIFY COLUMN `scar` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Toxoplasmosis scar presence: 1=present, 0=absent',
    MODIFY COLUMN `nevus` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Nevus presence: 1=present, 0=absent',
    MODIFY COLUMN `amd` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Age-related macular degeneration: 1=present, 0=absent',
    MODIFY COLUMN `vascular_occlusion` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Vascular occlusion: 1=present, 0=absent',
    MODIFY COLUMN `hypertensive_retinopathy` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Hypertensive retinopathy: 1=present, 0=absent',
    MODIFY COLUMN `drusens` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Drusens presence: 1=present, 0=absent',
    MODIFY COLUMN `hemorrhage` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Non-diabetic retinal hemorrhage: 1=present, 0=absent',
    MODIFY COLUMN `retinal_detachment` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Retinal detachment: 1=present, 0=absent',
    MODIFY COLUMN `myopic_fundus` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Myopic fundus: 1=present, 0=absent',
    MODIFY COLUMN `increased_cup_disc` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Increased cup-disc ratio: 1=present, 0=absent',
    MODIFY COLUMN `other` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Other retinal pathologies: 1=present, 0=absent',
    MODIFY COLUMN `quality` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Overall image quality assessment';

-- Add table and column comments for mbrest table
ALTER TABLE `mbrest`
    COMMENT 'mBRSET (Mobile Brazilian Retinal Dataset) - Contains retinal images captured via handheld camera for portable diabetic retinopathy screening.';

ALTER TABLE `mbrest`
    MODIFY COLUMN `patient` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Unique patient identifier',
    MODIFY COLUMN `age` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Age of the patient in years',
    MODIFY COLUMN `sex` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Gender of patient (Male/Female)',
    MODIFY COLUMN `dm_time` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Diabetes duration in years',
    MODIFY COLUMN `insulin` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Insulin therapy (Yes/No)',
    MODIFY COLUMN `insulin_time` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Duration of insulin therapy in years',
    MODIFY COLUMN `oraltreatment_dm` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Oral diabetes treatment (Yes/No)',
    MODIFY COLUMN `systemic_hypertension` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Systemic hypertension diagnosis (Yes/No)',
    MODIFY COLUMN `insurance` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Type of health insurance',
    MODIFY COLUMN `educational_level` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Highest education level completed',
    MODIFY COLUMN `alcohol_consumption` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Alcohol consumption habit (Yes/No)',
    MODIFY COLUMN `smoking` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Smoking status (Yes/No)',
    MODIFY COLUMN `obesity` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Obesity diagnosis (Yes/No)',
    MODIFY COLUMN `vascular_disease` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Vascular disease diagnosis (Yes/No)',
    MODIFY COLUMN `acute_myocardial_infarction` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'History of acute myocardial infarction (Yes/No)',
    MODIFY COLUMN `nephropathy` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Diabetic nephropathy (Yes/No)',
    MODIFY COLUMN `neuropathy` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Diabetic neuropathy (Yes/No)',
    MODIFY COLUMN `diabetic_foot` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Diabetic foot complications (Yes/No)',
    MODIFY COLUMN `file` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Image filename identifier',
    MODIFY COLUMN `laterality` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Which eye was examined (Left/Right)',
    MODIFY COLUMN `final_artifacts` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Presence of imaging artifacts (Yes/No)',
    MODIFY COLUMN `final_quality` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Overall image quality satisfactory for clinical assessment (Yes/No)',
    MODIFY COLUMN `final_icdr` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'International Clinic Diabetic Retinopathy classification: 0-4',
    MODIFY COLUMN `final_edema` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Diabetic macular edema presence (Yes/No)';