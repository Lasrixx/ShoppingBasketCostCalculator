class ShoppingBag:
    def calculate_bag_total(self, items, discounts):
        bag = {}
        cost = {}
        # Calculating the quantity of different items in the bag
        for item in items:
            itemCode = item[:3]
            itemCost = item[3:]
            if itemCode in bag:
                # If the item already exists in the bag, just increase quantity by 1
                itemQuant = bag.get(itemCode)
                costVal = cost.get(itemCode)
                bag.update({itemCode: int(itemQuant) + 1})
                cost.update({itemCode: int(costVal) + int(itemCost)})
            else:
                # If the item does not already exist, add it as a new itemCode
                bag[itemCode] = "1"
                cost[itemCode] = itemCost
        print(bag)
        print(cost)
        for discount in discounts:
            # Check item code and minimum quantity is met
            discountCode = discount[:3]
            minQuant = discount[3:4]
            if discountCode in bag and int(minQuant) <= int(bag[discountCode]):
                # Reduce cost by % or £ given
                discountMethod = discount[4:5]
                amountOff = discount[5:]
                if discountMethod == "P":
                    percentOff = (100 - int(amountOff)) / 100
                    discountedCost = int(cost[discountCode]) * percentOff
                    cost.update({discountCode: discountedCost})
                elif discountMethod == "C":
                    discountedCost = int(cost[discountCode]) - (int(amountOff) * int(bag[discountCode]))
                    cost.update({discountCode: discountedCost})
        totalCost = 0
        for item in cost:
            totalCost+=cost[item]
        return totalCost


solution = ShoppingBag()
print(solution.calculate_bag_total(["ABC010", "DEF020", "ABC010"], ["ABC2P50", "DEF1C05"]))
