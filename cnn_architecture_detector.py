from conv2D_call import Conv2DCall


def is_unet(no_of_filters: list[Conv2DCall]):
    print(no_of_filters)

    if len(no_of_filters) <= 2:
        return False

    if no_of_filters[-1].filters_value != 1:
        return False

   # check if all the values are same

    for i in range(int((len(no_of_filters)-1)/2)):
        if no_of_filters[i].filters_value != no_of_filters[-i-2].filters_value:
            return False

    return True
