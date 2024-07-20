def calculate_parking_charge(parking_duration):
    fixed_rate=55.0
    if parking_duration<=8.5:
        parking_charge=fixed_rate
    elif parking_duration<=23 :
        additional_locks=(parking_duration-8.5)//2
        parking_charge=fixed_rate+(additional_blocks*13.75)
    else:
        excess_duration=parking_duration-23
        parking_charge=fixed_rate+(14*13.75)+(excess_duration*5.50)
    return parking_charge
parking_duration=float(input('Enter the parking duration in hours: '))
charge_amount=clculate_parking_charge(parking_duration)
print(f'The parking charge is Rs. {charge_amount:.2f}')
            
