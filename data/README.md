# Dataset: 70K Job Applicants (HR Hiring Dataset)

## Overview

This project uses the **"70K Job Applicants Data – Human Resource"** dataset from Kaggle.
The raw data is **not committed to this repository** to avoid large file sizes and data leakage concerns.
All teammates must download the dataset themselves before running any notebooks.

---

## Quick Start: Download the Dataset

We provide a one-command download script that handles everything automatically:

```bash
python data/download_data.py
```

This script will:
1. Check that your Kaggle API key is set up (and explain how if not)
2. 2. Download the dataset directly from Kaggle
   3. 3. Unzip and rename the file to `data/raw/job_applicants.csv`
     
      4. ### First time? Set up your Kaggle API key:
      5. 1. Go to https://www.kaggle.com/settings
         2. 2. Scroll to **API** and click **Create New Token**
            3. 3. Move the downloaded `kaggle.json` to `~/.kaggle/kaggle.json`
               4. 4. Run `pip install kaggle` if you haven't already
                  5. 5. Then run `python data/download_data.py`
                    
                     6. ### Manual download (alternative):
                     7. 1. Visit: https://www.kaggle.com/datasets/ayushtankha/70k-job-applicants-data-human-resource
                        2. 2. Click **Download**, unzip, and place the CSV at `data/raw/job_applicants.csv`
                          
                           3. ---
                          
                           4. ## Column Descriptions
                          
                           5. | Column | Type | Description |
                           6. |--------|------|-------------|
                           7. | `Age` | Numeric | Age of the applicant (years) |
                           8. | `AccessToResources` | Numeric (1-5) | Applicant's access to resources/support |
                           9. | `AvgSessionDurationMinutes` | Numeric | Average time in training/assessment sessions |
                           10. | `Distance_from_Company` | Numeric | Distance from home to company (km) |
                           11. | `EducationLevel` | Categorical | Highest education level (High School, Bachelor's, Master's, PhD) |
                           12. | `ExperienceYears` | Numeric | Total years of relevant work experience |
                           13. | `Gender` | Categorical | Applicant's self-reported gender |
                           14. | `HiringDecision` | Binary (0/1) | **Target variable** — 1 = Hired, 0 = Not Hired |
                           15. | `InterviewScore` | Numeric (0-100) | Score from the interview process |
                           16. | `PreviousCompanies` | Numeric | Number of previous employers |
                           17. | `RecruitmentStrategy` | Categorical | Recruitment channel (e.g., Online, Referral) |
                           18. | `SkillScore` | Numeric (0-100) | Score from a standardised skills assessment |
                           19. | `WorkLifeBalance` | Numeric (1-5) | Self-reported work-life balance rating |
                          
                           20. ---
                          
                           21. ## Feature Groups (for our 4 experiments)
                          
                           22. | Group | Features | Experiment |
                           23. |-------|----------|------------|
                           24. | **Education** | `EducationLevel` | Experiment 1 |
                           25. | **Experience** | `ExperienceYears`, `PreviousCompanies` | Experiment 2 |
                           26. | **Skills** | `SkillScore` | Experiment 3 |
                           27. | **Combined** | All above + `Age`, `Gender`, `Distance_from_Company`, `InterviewScore`, `AccessToResources`, `AvgSessionDurationMinutes`, `WorkLifeBalance`, `RecruitmentStrategy` | Experiment 4 |
                          
                           28. ---
                          
                           29. ## Processed Outputs (committed to repo)
                          
                           30. After running `notebooks/01_data_preprocessing.ipynb`, these files are saved to `data/processed/`:
                          
                           31. | File | Description |
                           32. |------|-------------|
                           33. | `train_education.csv` | Train split - education features only |
                           34. | `test_education.csv` | Test split - education features only |
                           35. | `train_experience.csv` | Train split - experience features only |
                           36. | `test_experience.csv` | Test split - experience features only |
                           37. | `train_skills.csv` | Train split - skills features only |
                           38. | `test_skills.csv` | Test split - skills features only |
                           39. | `train_combined.csv` | Train split - all features |
                           40. | `test_combined.csv` | Test split - all features |
                          
                           41. ---
                          
                           42. ## Data Leakage Note
                          
                           43. We only use features available **before** a hiring decision is made. `HiringDecision` is the target only — never a feature.
