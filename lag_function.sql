select  top 100
dt
,month(Dt)
,[GC=F_Close]
,lag([GC=F_Close]) over (order by month(dt)) as [prev_dt]
,lag([GC=F_Close]) over(order by year(dt)) as [prev_yr)
 from dbo.Stocks
 group by month(dt)
 order by dt desc

 ;with lst_mnth_gld
 as 
 (
 select top 100
 s.dt
 ,DATEPART(MONTH, s.dt) mnth
 ,sum(s.[GC=F_Close]) as [gld_close]
 from dbo.Stocks s 
 group by datepart(month, s.dt), s.dt
 order by s.dt,DATEPART(MONTH, s.dt)   desc
 )select
 dt
 ,mnth
 ,lag(gld_close, 1, 0) over (order by mnth) [lst_mnt]
 ,lag(gld_close, 1, 0) over (order by year(dt)) [lst_yr]
 ,lag(dt) over (order by year(dt)) lst_Yr
 ,gld_close
 from lst_mnth_gld
 
 select top 100 * from dbo.Stocks

 select 
 FullDateAlternateKey ,
 lag(FullDateAlternateKey, 1) over (order by FullDateAlternateKey )
 from AdventureWorksDW2019.dbo.DimDate


alter table dbo.Stocks add dt date
update dbo.stocks
update dbo.Stocks set dt = format(Date_ , 'yyyy-MM-dd') 

select DATEPART(i, getdate())

select format(getdate(), 'yyyy-MM-dd')


select 
rank() over (order by SI_Close desc)
,dt
from dbo.Commodity

update dbo.Commodity set dt = convert(date , dt, 101)


select  convert(date, getdate(), 101)