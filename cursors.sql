declare @dt_ varchar(10)
declare @YoY varchar(10)
declare Largest cursor for
select cast(dt as varchar(10)), cast(Yoy as varchar(10)) from dbo.CPI_All
open Largest 
while @@FETCH_STATUS=0
begin
	print 'loop'
	print @dt_ + @YoY
	fetch next from Larges into @dt_, @YoY
	
	end
close Largest
deallocate Largest

DECLARE @dt_ varchar(50);
DECLARE @YoY varchar(50);
DECLARE BLS CURSOR FOR
SELECT dt, Yoy
FROM dbo.CPI_All
OPEN BLS;

FETCH NEXT FROM BLS INTO @dt_, @YoY;

WHILE @@FETCH_STATUS = 0
BEGIN
    PRINT @dt_ + @YoY
    -- Perform other operations here, e.g., UPDATE statements

    FETCH NEXT FROM BLS INTO @dt_, @YoY;
END;

CLOSE BLS;
DEALLOCATE BLS



