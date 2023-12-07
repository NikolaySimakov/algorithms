-- name: Success collector
-- total_sales: 152380


select st.name, sum(pt.price) as total_sales
from transactions as tt 

join users as ut
on tt.user_id = ut.id 

join cities as ct 
on ct.id = ut.city_id 

join products as pt 
on pt.id = tt.product_id 

join sellers as st 
on st.id = pt.seller_id 

where ct.name = 'Krasnodar' and tt.status = 'completed' 
group by st.name 
order by total_sales desc 