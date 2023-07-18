INSERT INTO company_info VALUES (%s, %s, %s)
INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s)
SELECT company_name, count_vacancy FROM company_info
SELECT  company_name, vacancy_name, salary_from, salary_to, url FROM vacancies INNER JOIN company_info USING (company_id)
SELECT company_name, ROUND(AVG(salary_from)) FROM vacancies INNER JOIN company_info USING (company_id) WHERE salary_from > 0 GROUP BY company_name
SELECT vacancy_name, url FROM vacancies WHERE salary_from > (SELECT AVG(salary_from) FROM vacancies)
SELECT vacancy_name, url FROM vacancies WHERE vacancy_name LIKE '%ython%'

