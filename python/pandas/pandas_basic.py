import pandas
df = pandas.read_csv("csv/file_1.csv", delimiter='|', dtype = str)


def first_letter(row):
    return row['first_name'].title()

def replace_country_code(row):

    if "FRA" in row['country_code']:
        return "France"
    if "CHE" in row['country_code']:
        return "Suisse"

def add_phone_indicator(row):
    mobile_phone_str = str(row['mobile_phone'])
    if not (mobile_phone_str == "nan"):
        mobile_phone_str = mobile_phone_str.replace('-','')
        mobile_phone_str = mobile_phone_str.replace(' ', '')

        if (mobile_phone_str[0] == "0"):
            mobile_phone_str = mobile_phone_str.replace('0', '+33', 1)

        if (len(mobile_phone_str) == 11) and mobile_phone_str[0:2] == "33":
            mobile_phone_str = mobile_phone_str.replace('33', '+33', 1)

        return mobile_phone_str

df['norm_first_name'] = df.apply(first_letter, axis=1)
df['norm_country_code'] = df.apply(replace_country_code, axis=1)
df['norm_mobile_phone'] = df.apply(add_phone_indicator, axis=1)



df.to_csv("csv/file_2.csv", sep='|')