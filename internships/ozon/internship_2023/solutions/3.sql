-- name: Nicole
-- purchases: 4


select ut.name, count(tt.id) as purchases
from transactions as tt 

join users as ut
on tt.user_id = ut.id 

join cities as ct 
on ct.id = ut.city_id 

where ct.name = 'Sochi' and tt.status = 'completed' and EXTRACT(YEAR FROM tt.created_at) = 2021 AND EXTRACT(MONTH FROM tt.created_at) = 2
-- WHERE YEAR(tt.created_at) = 2021 AND MONTH(tt.created_at) = 2
group by ut.name
order by purchases desc limit 1