def tip(bill , tip_perc):
    total=bill*(1+0.01*tip_perc)
    total=round(total, 2)
    print("You need to pay ", total)
tip(150, 20)