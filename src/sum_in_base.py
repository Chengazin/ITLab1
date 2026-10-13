def add_in_base(a: str, b: str, base: int) -> str:
    """
                Складывает два числа, записанных в системе счисления с основанием base.
            
                :param a: первое число, строка (например, "1011")
                :param b: второе число, строка (например, "111")
                :param base: основание системы счисления, 2 <= base <= 36
                :return: сумма в той же системе счисления, строка
            
                Пример:
                    add_in_base("1011", "111", 2) -> "10010"
                    add_in_base("FF", "1", 16) -> "100"
                """
    if not (2 <= base <= 36):
       raise ValueError("Основание должно быть от 2 до 36")            
    try:
        
        digits= "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        num1= int(a,base)
        num2 = int(b,base)
        resnum=num1+num2
        if resnum ==0:
            return "0"
        res =""
        while resnum > 0:
            res = digits[resnum % base] + res
            resnum //= base
        return res
    except TypeError:
        return("Неверный тип данных. Введите заново")
    
    
print(add_in_base("Z", "1", 37))