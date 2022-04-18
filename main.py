### 1. Tiger reserves in india
### 2. Canedian Election Results from plotly datasets
import TigerReserves as TR
import CanedianElection as CN

print('Select 1 among below 2 options-')
print("Option 1: Map Tiger Reserves in India on Map")
print("Option 2: Map Canadian Election Result on Map")
option=int(input())

if(option==1):
    TR.Tiger_Reserves()

elif(option==2):
    CN.Canedian_Election()

else:
    print("Please Enter Valid Option")