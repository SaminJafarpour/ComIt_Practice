'''various kinds of vehicles are built with this class'''
class Vehicle:
    

    def __init__(self, kind:str, price:int, VAT:int=0):
        self.kind=kind
        self.price=price
        self.VAT=VAT
        if price>100000000:
            self.VAT=0.20*100000000
        else:
            self.VAT=0.16*100000000
        print(f"VAT for this car is: {self.VAT}")
    
    def calculating_final_value(self,final_value)->None:
        self.final_value=final_value
        additional_discount:int
        if self.final_value<80000000:
            additional_discount=self.final_value*0.05
            print(f"eligible for additional discount of 5% and the final price is {self.final_value-additional_discount}")
        else:
            print("your vehicle is not eligible for any discount")
        
      
            



type1=Vehicle("family_cars",75000000)
if type1.price<=50000000:
    primery_discount=0.5*type1.VAT
    print(f"this vehicle is eligible for {primery_discount} discount")
else:
    primery_discount=0
    print("this car is not eligible for primery discount")
type1.final_value=type1.price-primery_discount
type1.calculating_final_value(type1.final_value)



type2=Vehicle("public_transportation",110000000)
if type2.price>=80000000:
    additional_cost=0.05*type2.price
    print(f"this vehicle is subjected to {additional_cost} additional cost")
else:
    additional_cost=0
type2.final_value=additional_cost+type2.price

type2.calculating_final_value(type2.final_value)

type3=Vehicle("load_vehicle",110000000)
if type3.price>=80000000:
    additional_cost=0.05*type3.price
    print(f"this vehicle is subjected to {additional_cost} additional cost")
else:
    additional_cost=0
type3.final_value=additional_cost+type3.price

type3.calculating_final_value(type3.final_value)