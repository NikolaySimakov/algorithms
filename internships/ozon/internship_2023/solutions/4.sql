
-- Gleb
-- total_sales: 25750
-- month: 1


-- Igor
-- total_sales: 50485
-- month: 3


-- Nicole
-- total_sales: 24466
-- month: 2


select sum(pt.price) as total_sales, EXTRACT(MONTH FROM tt.created_at) as month
from transactions as tt 

join users as ut
on tt.user_id = ut.id 

join cities as ct 
on ct.id = ut.city_id 

join products as pt 
on pt.id = tt.product_id 

join sellers as st 
on st.id = pt.seller_id 

where tt.status = 'completed' and ut.name = 'Gleb'
-- or ut.name = 'Igor' or ut.name = 'Nicole'
group by EXTRACT(MONTH FROM tt.created_at)