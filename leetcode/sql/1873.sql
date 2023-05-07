-- select entries with odd  employee id and name not start with M
select employee_id, salary as bonus 
from employees 
where employee_id%2 <>0 and name not like 'M%'

-- join both selection 
union

-- select remaining entries from table 
select employee_id, 0 as bonus
from employees
where employee_id%2 = 0 or name like 'M%'
order by employee_id;