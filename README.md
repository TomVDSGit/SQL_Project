# SQL Project 
## Introduction
Questions to Answer:
1. What are the top-paying jobs for a Data Analyst? [SQL File](/project_sql/1_top_paying_jobs.sql)
2. What are the skills required for these top-paying roles? [SQL File](/project_sql/2_top_paying_jobs_skills.sql)
3. What are the most in-demand skills for a Data Analyst? [SQL File](/project_sql/3_top_demanded_skills.sql)
4. What are the top skills based on salary for a Data Analyst? [SQL File](/project_sql/4_top_paying_skills.sql)
5. What are the most optimal skills to learn? [SQL File](/project_sql/5_optimal_skills.sql)
6. What are the jobs that are specific to me? [SQL File](/project_sql/6_specific_jobs.sql)

Data is provided by Luke Barousse through his [SQL Course](https://lukebarousse.com/sql). 

## Software I Used
For my analysis of the data analyst job market, I used several key tools:

- **SQL:** The backbone of my analysis, allowing me to query the database and unearth critical insights.
- **PostgreSQL:** The chosen database management system, ideal for handling the job posting data.
- **Visual Studio Code:** My go-to for database management, executing SQL queries and carrying out python analysis.
- **Git & GitHub:** Essential for version control and sharing my SQL scripts and analysis, ensuring collaboration and project tracking.

### 1. Top Paying Data Analyst Jobs
To identify the highest-paying roles, I filtered data analyst positions by average yearly salary and location, focusing on remote jobs. This query highlights the high paying opportunities in the field.

```sql
SELECT
    jpf.job_id, 
    jpf.job_title, 
    jpf.job_location, 
    jpf.job_schedule_type, 
    jpf.salary_year_avg, 
    jpf.job_posted_date,
    c.name AS company_name
FROM 
    job_postings_fact AS jpf
LEFT JOIN company_dim AS c ON jpf.company_id = c.company_id
WHERE
    job_title_short = 'Data Analyst' AND
    job_location = 'Anywhere' AND
    salary_year_avg IS NOT NULL
ORDER BY
    salary_year_avg DESC
LIMIT 10;
```
Through Python, I created a bar chart of the top 10 salaries for data analyst jobs. The plotting code can be found here: [Top 10 Data Analyst Jobs](project_sql/1_top_paying_jobs.py)

![Top Paying Roles](project_sql/Q1_fig.png)
*Bar graph visualizing the salary for the top 10 salaries for data analysts*
 
 ### 2. Skills for Top Paying Jobs
To understand what skills are required for the top-paying jobs, I joined the job postings with the skills data, providing insights into what employers value for high-compensation roles.
```sql
WITH top_paying_jobs AS (
    SELECT
        jpf.job_id, 
        jpf.job_title, 
        jpf.salary_year_avg, 
        c.name AS company_name
    FROM 
        job_postings_fact AS jpf
    LEFT JOIN company_dim AS c ON jpf.company_id = c.company_id
    WHERE
        job_title_short = 'Data Analyst' AND
        job_location = 'Anywhere' AND
        salary_year_avg IS NOT NULL
    ORDER BY
        salary_year_avg DESC
    LIMIT 10
)

SELECT 
    top_paying_jobs.*,
    skills_dim.skills
FROM top_paying_jobs
INNER JOIN skills_job_dim ON top_paying_jobs.job_id = skills_job_dim.job_id
INNER JOIN skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id
ORDER BY 
    salary_year_avg DESC;
```

Through Python, I created a bar chart of the top 10 skills for data analyst jobs. The plotting code can be found here: [Top 10 Skills](project_sql/2_top_paying_jobs_skills.py)

![Top Paying Skills](project_sql/Q2_fig.png)
*Bar graph visualizing the count of skills for the top 10 paying jobs for data analysts*

### 3. In-Demand Skills for Data Analysts

This query helped identify the skills most frequently requested in job postings, directing focus to areas with high demand.

```sql
SELECT 
    skills,
    COUNT(skills_job_dim.job_id) AS demand_count
FROM job_postings_fact
INNER JOIN skills_job_dim ON job_postings_fact.job_id = skills_job_dim.job_id
INNER JOIN skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id
WHERE
    job_title_short = 'Data Analyst' 
--  AND job_work_from_home = TRUE
GROUP BY 
    skills
ORDER BY 
    demand_count DESC
LIMIT 5;
```

| Skills   | Demand Count |
|----------|--------------|
| SQL      | 92628         |
| Excel    | 67031         |
| Python   | 57326         |
| Tableau  | 46554         |
| Power BI | 39468         |

*Table of the demand for the top 5 skills in data analyst job postings*