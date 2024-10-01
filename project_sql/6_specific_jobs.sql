/*
Question: What are the jobs that are specific to my requirements?
- Search for data jobs that are in the UK and that are full-time.
- Refine the jobs for a university graduate.
*/

SELECT
    jpf.job_id, 
    jpf.job_title, 
    c.name AS company_name,
    jpf.job_location, 
    jpf.job_schedule_type, 
    jpf.salary_year_avg, 
    jpf.job_posted_date
FROM 
    job_postings_fact AS jpf
LEFT JOIN company_dim AS c ON jpf.company_id = c.company_id
WHERE
    jpf.job_title LIKE '%Data%' AND
    jpf.job_title NOT LIKE '%Senior%' AND 
    jpf.job_title NOT LIKE '%Lead%' AND
    jpf.job_title NOT LIKE '%Director%' AND
 --   (jpf.job_title LIKE '%Graduate%' OR jpf.job_title LIKE '%Junior%') AND
    jpf.job_country = 'United Kingdom' AND
    jpf.job_schedule_type = 'Full-time' AND
    jpf.salary_year_avg IS NOT NULL