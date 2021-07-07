import pandas as pd
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox

'''
# Validation for HSC
'''
def HSC_Validate(self, df_):
    global df, table_result

    filterString = self.lineEdit_2.text()
    
    df = df_.loc[df_['col_12'] == filterString]
    print(df)

    #df = df.dropna(subset=['col_18', 'col_19'], inplace=True)
    
    print('Entered HSC_Validate')

    # Modified Checks of HSC

    # 4.3 (56) <= 2.1.1.a (39) + 2.1.1.b (40) + 2.2 (43) (For recurring data items)
    def res1(df):

        # If all elements are null
        if pd.isnull(df['col_56']) and pd.isnull(df['col_39']) and pd.isnull(df['col_40']) and pd.isnull(df['col_43']):
            return 'Blank'

        # If any one element is null
        elif pd.isnull(df['col_56']) or pd.isnull(df['col_39']) or pd.isnull(df['col_40']) or pd.isnull(df['col_43']):
            if pd.isnull(df['col_56']) and not pd.isnull(float(df['col_39']) + float(df['col_40']) + float(df['col_43'])):
                return 'Probable Reporting Error'
            else:
                if pd.isnull(float(df['col_39']) + float(df['col_40']) + float(df['col_43'])) and not pd.isnull(df['col_56']):
                    return 'Probable Reporting Error'
                else:
                    return 'Probable Reporting Error'

        # If value exists for all the elements
        else:
            lhs_value = float(df['col_56'])
            rhs_value = float(df['col_39']) + \
                float(df['col_40']) + float(df['col_43'])

            if lhs_value <= rhs_value:
                if lhs_value < (0.5*rhs_value):
                    return 'Probable Reporting Error'
                else:
                    return 'consistent'
            else:
                if lhs_value > (0.5*rhs_value):
                    return 'Probable Reporting Error'
                else:
                    return 'Inconsistent'
        return df

    # 1.1(col_22) >= 1.1.1(col_23) (for related data items)
    def res2(df):
        if pd.isnull(df['col_22']) and pd.isnull(df['col_23']):
            return 'Blank'
        elif pd.isnull(df['col_22']) or pd.isnull(df['col_23']):
            if pd.isnull(df['col_22']):
                return 'Inconsistent'
            elif pd.isnull(df['col_23']):
                return 'Probable Reporting Error (1.1.1 is blank)'
        elif df['col_22'] < df['col_23']:
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 1.3.1.a(col_33) <= 1.3.1(col_32) (for related data items)

    def res3(df):
        if (df['col_33'] is None) and (df['col_32'] is None):
            return 'Blank'
        elif (df['col_33'] is None) or (df['col_32'] is None):
            if (df['col_33'] is None):
                return 'Inconsistent'
            elif (df['col_32'] is None):
                return 'Probable Reporting Error (1.3.1 is blank)'
        if (df['col_33'] is None) > (df['col_32'] is None):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    #  1.2.7 (30) <= 1.1(22) (For recurring data items)
    def res4(df):
        if pd.isnull(float(df['col_30'])) and pd.isnull(float(df['col_22'])):
            return 'Blank'
        elif pd.isnull(float(df['col_30'])) or pd.isnull(float(df['col_22'])):
            if pd.isnull(df['col_30']):
                return 'Inconsistent'
            elif pd.isnull(df['col_22']):
                return 'Probable Reporting Error (1.1 is blank)'
        # If value exists for all the elements
        else:

            lhs_value = float(df['col_30'])
            rhs_value = float(df['col_22'])

            if lhs_value <= rhs_value:
                if lhs_value < (0.5*rhs_value):
                    return 'Probable Reporting Error'
                else:
                    return 'consistent'
            else:
                if lhs_value > (0.5*rhs_value):
                    return 'Probable Reporting Error'
                else:
                    return 'Inconsistent'
        return df

    # # 1.5.1.a (37) <= 1.1 (22) (for unrelated data items)
    def res5(df):
        if pd.isnull(float(df['col_37'])) and pd.isnull(float(df['col_22'])):
            return 'Blank'
        elif pd.isnull(float(df['col_37'])) or pd.isnull(float(df['col_22'])):
            if pd.isnull(df['col_37']):
                return 'Probable Reporting Error(1.5.1.a is blank)'
            elif pd.isnull(df['col_22']):
                return 'Inconsistent (1.1 is blank)'
        elif float(df['col_37']) > float(df['col_22']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 1.5.1.b (col_38) <= 1.5.1.a (col_37) (for related data items)
    def res6(df):

        if pd.isnull(float(df['col_38'])) and pd.isnull(float(df['col_37'])):
            return 'Blank'
        elif pd.isnull(float(df['col_38'])) or pd.isnull(float(df['col_37'])):
            if pd.isnull(df['col_38']):
                return 'Probable Reporting Error (1.5.1.b is blank)'
            elif pd.isnull(df['col_37']):
                return 'Inconsistent (1.5.1.a is blank)'
        elif float(df['col_38']) > float(df['col_37']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

        # 2.1.2 (col_41) <= 2.1.1.a(col_39) + 2.1.1.b(col_40) (for unrelated data items)
    def res7(df):
        if pd.isnull(df['col_41']) and pd.isnull(df['col_39']) and pd.isnull(df['col_40']):
            return 'Blank'
        elif pd.isnull(df['col_41']) or pd.isnull(df['col_39']) or pd.isnull(df['col_40']):
            if pd.isnull(df['col_41']):
                return 'Probable Reporting Error (2.1.2 is blank)'
            elif pd.isnull(df['col_39']):
                return 'Inconsistent 2.1.1.a is null'
            elif pd.isnull(df['col_40']):
                return 'Inconsistent 2.1.1.b is null'
        elif float(df['col_41']) > float(df['col_39']) + float(df['col_40']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

        # 2.1.3 (col_42) <= 2.1.1.a(col_39) + 2.1.1.b(col_40) (For recurring data items)
    def res8(df):

        if pd.isnull(df['col_42']) and pd.isnull(df['col_39']) and pd.isnull(df['col_40']):
            return 'Blank'
        elif pd.isnull(df['col_42']) or pd.isnull(df['col_39']) or pd.isnull(df['col_40']):
            if pd.isnull(df['col_42']) and not pd.isnull(float(df['col_39']) + float(df['col_40'])):
                return 'Probable Reporting Error'
            else:
                if pd.isnull(float(df['col_39']) + float(df['col_40'])) and not pd.isnull(df['col_42']):
                    return 'Probable Reporting Error'
                else:
                    return 'Probable Reporting Error'

        # If value exists for all the elements
        else:

            lhs_value = float(df['col_42'])
            rhs_value = float(df['col_39']) + float(df['col_40'])

            if lhs_value <= rhs_value:
                if lhs_value < (0.5*rhs_value):
                    return 'Probable Reporting Error'
                else:
                    return 'consistent'
            else:
                if lhs_value > (0.5*rhs_value):
                    return 'Probable Reporting Error'
                else:
                    return 'Inconsistent'
        return df

    # 2.2.2(col_45) <= 2.2 (col_43) (For recurring data items) ----------need update
    def res9(df):
        if pd.isnull(df['col_45']) and pd.isnull(df['col_43']):
            return 'Blank'
        elif pd.isnull(df['col_45']) or pd.isnull(df['col_43']):
            if pd.isnull(df['col_45']) and not pd.isnull(float(df['col_43'])):
                return 'Probable Reporting Error'
            else:
                if pd.isnull(float(df['col_43'])) and not pd.isnull(df['col_45']):
                    return 'Probable Reporting Error'
                else:
                    return 'Probable Reporting Error'

        # If value exists for all the elements
        else:

            lhs_value = float(df['col_45'])
            rhs_value = float(df['col_43'])

            if lhs_value <= rhs_value:
                if lhs_value < (0.5*rhs_value):
                    return 'Probable Reporting Error'
                else:
                    return 'consistent'
            else:
                if lhs_value > (0.5*rhs_value):
                    return 'Probable Reporting Error'
                else:
                    return 'Inconsistent'
        return df

    # 4.4(col_57)<= 2.1.1.a(col_39) + 2.1.1.b(col_40) + 2.2(col_43) (For recurring data items)
    def res10(df):
        if pd.isnull(df['col_57']) and pd.isnull(df['col_39']) and pd.isnull(df['col_40']) and pd.isnull(df['col_43']):
            return 'Blank'
        elif pd.isnull(df['col_57']) and pd.isnull(df['col_39']) and pd.isnull(df['col_40']) and pd.isnull(df['col_43']):
            if pd.isnull(df['col_57']) and not pd.isnull(float(df['col_39']) + float(df['col_40']) + float(df['col_43'])):
                return 'Probable Reporting Error'
            else:
                if pd.isnull(float(df['col_39']) + float(df['col_40']) + float(df['col_43'])) and not pd.isnull(df['col_42']):
                    return 'Probable Reporting Error'
                else:
                    return 'Probable Reporting Error'

        # If value exists for all the elements
        else:

            lhs_value = float(df['col_57'])
            rhs_value = float(df['col_39']) + \
                float(df['col_40']) + float(df['col_43'])

            if lhs_value <= rhs_value:
                if lhs_value < (0.5*rhs_value):
                    return 'Probable Reporting Error'
                else:
                    return 'consistent'
            else:
                if lhs_value > (0.5*rhs_value):
                    return 'Probable Reporting Error'
                else:
                    return 'Inconsistent'
        return df

        # 6.1.1(col_73) <= 3.1.1.a(col_46) + 3.1.1.b(col_47)
    def res11(df):
        if pd.isnull(df['col_73']) and pd.isnull(df['col_46']) and pd.isnull(df['col_47']):
            return 'Blank'
        elif pd.isnull(df['col_73']) or pd.isnull(df['col_46']) or pd.isnull(df['col_47']):
            if pd.isnull(df['col_73']):
                return 'Probable Reporting Error (6.1.1 is blank)'
            elif pd.isnull(df['col_46']):
                return 'Inconsistent (3.1.1.a is blank)'
            elif pd.isnull(df['col_47']):
                return 'Inconsistent (3.1.1.b is blank)'
        elif float(df['col_73']) > float(df['col_46']) + float(df['col_47']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 6.1.9(col_81) <= 3.1.1.a(col_46) + 3.1.1.b(col_47)
    def res12(df):

        if pd.isnull(df['col_81']) and pd.isnull(df['col_46']) and pd.isnull(df['col_47']):
            return 'Blank'
        elif pd.isnull(df['col_81']) or pd.isnull(df['col_46']) or pd.isnull(df['col_47']):
            if pd.isnull(df['col_81']):
                return 'Probable Reporting Error (6.1.9 is blank)'
            elif pd.isnull(df['col_46']):
                return 'Inconsistent (3.1.1.a is blank)'
            elif pd.isnull(df['col_47']):
                return 'Inconsistent (3.1.1.b is blank)'
        elif float(df['col_81']) > float(df['col_46']) + float(df['col_47']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 6.1.13(col_85) <= 3.1.1.a(col_46) + 3.1.1.b(col_47)
    def res13(df):
        if pd.isnull(df['col_85']) and pd.isnull(df['col_46']) and pd.isnull(df['col_47']):
            return 'Blank'
        elif pd.isnull(df['col_85']) or pd.isnull(df['col_46']) or pd.isnull(df['col_47']):
            if pd.isnull(df['col_85']):
                return 'Probable Reporting Error  (6.1.13 is blank)'
            elif pd.isnull(df['col_46']):
                return 'Inconsistent (6.1.13 is blank)'
            elif pd.isnull(df['col_47']):
                return 'Inconsistent (6.1.13 is blank)'
        elif float(df['col_85']) > float(df['col_46']) + float(df['col_47']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 2.2.1(col_44) <= 2.2(col_43)
    def res14(df):
        if pd.isnull(df['col_44']) and pd.isnull(df['col_43']):
            return 'Blank'
        elif pd.isnull(df['col_44']) or pd.isnull(df['col_43']):
            if pd.isnull(df['col_44']):
                return 'Probable Reporting Error (2.2.1 is blank)'
            elif pd.isnull(df['col_43']):
                return 'Inconsistent (2.2 is blank)'
        elif float(df['col_44']) > float(df['col_43']):
            return 'Inconsistent (check fails)'
        else:
            return 'consistent'
        return df

        # 3.1.2(col_48) <= 3.1.1.a(col_46)+ 3.1.1.b(col_47)
    def res15(df):
        if pd.isnull(df['col_48']) and pd.isnull(df['col_46']) and pd.isnull(df['col_47']):
            return 'Blank'
        elif pd.isnull(df['col_48']) or pd.isnull(df['col_46']) or pd.isnull(df['col_47']):
            if pd.isnull(df['col_48']):
                return 'Probable Reporting Error (3.1.2 is blank)'
            elif pd.isnull(df['col_46']):
                return 'Inconsistent(3.1.1.a is blank)'
            elif pd.isnull(df['col_47']):
                return 'Inconsistent (3.1.1.b is blank)'
        elif float(df['col_48']) > float(df['col_46']) + float(df['col_47']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

        # 3.3.1 <= 3.1.1.a + 3.1.1.b
    def res16(df):

        if pd.isnull(df['col_51']) and pd.isnull(df['col_46']) and pd.isnull(df['col_47']):
            return 'Blank'
        elif pd.isnull(df['col_51']) or pd.isnull(df['col_46']) or pd.isnull(df['col_47']):
            if pd.isnull(df['col_51']):
                return 'Probable Reporting Error (3.3.1 is blank)'
            elif pd.isnull(df['col_46']):
                return 'Inconsistent (3.3.1.a is blank)'
            elif pd.isnull(df['col_47']):
                return 'Inconsistent (3.3.1.b is blank)'
        elif float(df['col_51']) > float(df['col_46']) + float(df['col_47']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

        # 3.3.2 <= 3.3.1
    def res17(df):
        if pd.isnull(df['col_52']) and pd.isnull(df['col_51']):
            return 'Blank'
        elif pd.isnull(df['col_52']) or pd.isnull(df['col_51']):
            if pd.isnull(df['col_52']):
                return 'Probable Reporting Error (3.3.2 is blank)'
            elif pd.isnull(df['col_67']):
                return 'Inconsistent (3.3.1 is blank)'
        if float(df['col_52']) > float(df['col_51']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 3.3.3<=3.1.1.a+3.1.1.b
    def res18(df):

        if pd.isnull(df['col_53']) and pd.isnull(df['col_46']) and pd.isnull(df['col_47']):
            return 'Blank'
        elif pd.isnull(df['col_53']) or pd.isnull(df['col_46']) or pd.isnull(df['col_47']):
            if pd.isnull(df['col_53']):
                return 'Probable Reporting Error (3.3.3 is blank)'
            elif pd.isnull(float(df['col_46']) + float(df['col_47'])):
                return 'Inconsistent'
        elif float(df['col_53']) > float(df['col_46']) + float(df['col_47']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

        # 4.1 <= 2.1.1.a + 2.1.1.b
    def res19(df):

        if pd.isnull(df['col_54']) and pd.isnull(df['col_39']) and pd.isnull(df['col_40']):
            return 'Blank'
        elif pd.isnull(df['col_54']) or pd.isnull(df['col_39']) or pd.isnull(df['col_40']):
            if pd.isnull(df['col_54']):
                return 'Probable Reporting Error(4.1 is blank)'
            elif pd.isnull(float(df['col_39']) + float(df['col_40'])):
                return 'Inconsistent'
        elif float(df['col_54']) > float(df['col_39']) + float(df['col_40']):
            return 'Inconsistent (check fails)'
        else:
            return 'consistent'
        return df

    # 5.2 <= 2.1.1.a + 2.1.1.b + 2.2
    def res20(df):

        if pd.isnull(df['col_59']) and pd.isnull(df['col_39']) and pd.isnull(df['col_40']) and pd.isnull(df['col_43']):
            return 'Blank'
        elif pd.isnull(df['col_59']) or pd.isnull(df['col_39']) or pd.isnull(df['col_40']) or pd.isnull(df['col_43']):
            if pd.isnull(df['col_59']):
                return 'Probable Reporting Error(5.2 is blank)'
            elif pd.isnull(float(df['col_39']) + float(df['col_40']) + float(df['col_43'])):
                return 'Inconsistent'
        elif float(df['col_59']) > float(df['col_39']) + float(df['col_40']) + float(df['col_43']):
            return 'Inconsistent (check fails)'
        else:
            return 'consistent'
        return df

        # 6.2.4.a + 6.2.4.b <= 6.2.1 + 6.2.2
    def res21(df):

        if pd.isnull(df['col_97']) and pd.isnull(df['col_98']) and pd.isnull(df['col_94']) and pd.isnull(df['col_95']):
            return 'Blank'
        elif pd.isnull(df['col_97']) or pd.isnull(df['col_98']) or pd.isnull(df['col_94']) or pd.isnull(df['col_95']):
            if pd.isnull(df['col_97']):
                return 'Probable Reporting Error (6.2.4.a is blank)'
            elif pd.isnull(float(df['col_94']) + float(df['col_95'])):
                return 'Probable Reporting Error'
        elif float(df['col_97']) + float(df['col_98']) > float(df['col_94']) + float(df['col_95']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 6.6.1<=6.1.1+6.1.2+6.1.3+6.1.4+6.1.5+6.1.6+6.1.7+6.1.8+6.1.13+6.1.14+6.1.15+6.1.16+6.1.17+6.1.18+6.1.19+6.1.20+6.1.21+6.2.1+6.2.2+6.2.3+6.3.1+6.3.2+6.3.3+6.4.1+6.4.2+6.4.3+6.4.5+6.4.6+6.5.1+6.5.2+6.5.3+6.5.4
    def res22(df):

        if pd.isnull(df['col_112']) and pd.isnull(df['col_73']) and pd.isnull(df['col_74']) and pd.isnull(df['col_75']) and pd.isnull(df['col_76']) and pd.isnull(df['col_77']) and pd.isnull(df['col_78']) and pd.isnull(df['col_79']) and pd.isnull(df['col_80']) and pd.isnull(df['col_85']) and pd.isnull(df['col_86']) and pd.isnull(df['col_87']) and pd.isnull(df['col_88']) and pd.isnull(df['col_89']) and pd.isnull(df['col_90']) and pd.isnull(df['col_91']) and pd.isnull(df['col_92']) and pd.isnull(df['col_93']) and pd.isnull(df['col_94']) and pd.isnull(df['col_95']) and pd.isnull(df['col_96']) and pd.isnull(df['col_99']) and pd.isnull(df['col_100']) and pd.isnull(df['col_101']) and pd.isnull(df['col_102']) and pd.isnull(df['col_103']) and pd.isnull(df['col_104']) and pd.isnull(df['col_106']) and pd.isnull(df['col_107']) and pd.isnull(df['col_108']) and pd.isnull(df['col_109']) and pd.isnull(df['col_110']):
            return 'Blank'
        elif pd.isnull(df['col_112']) or pd.isnull(df['col_73']) or pd.isnull(df['col_74']) or pd.isnull(df['col_75']) or pd.isnull(df['col_76']) or pd.isnull(df['col_77']) or pd.isnull(df['col_78']) or pd.isnull(df['col_79']) or pd.isnull(df['col_80']) or pd.isnull(df['col_85']) or pd.isnull(df['col_86']) or pd.isnull(df['col_87']) or pd.isnull(df['col_88']) or pd.isnull(df['col_89']) or pd.isnull(df['col_90']) or pd.isnull(df['col_91']) or pd.isnull(df['col_92']) or pd.isnull(df['col_93']) or pd.isnull(df['col_122']) or pd.isnull(df['col_94']) or pd.isnull(df['col_96']) or pd.isnull(df['col_99']) or pd.isnull(df['col_100']) or pd.isnull(df['col_101']) or pd.isnull(df['col_102']) or pd.isnull(df['col_103']) or pd.isnull(df['col_104']) or pd.isnull(df['col_106']) or pd.isnull(df['col_107']) or pd.isnull(df['col_108']) or pd.isnull(df['col_109']) or pd.isnull(df['col_110']):
            if pd.isnull(df['col_112']):
                return 'Probable Reporting Error (6.6.1 is blank)'
            elif pd.isnull(float(df['col_73']) + float(df['col_74']) + float(df['col_75']) + float(df['col_76']) + float(df['col_77']) + float(df['col_78']) + float(df['col_79']) + float(df['col_80']) + float(df['col_85']) + float(df['col_86']) + float(df['col_87']) + float(df['col_88']) + float(df['col_89']) + float(df['col_90']) + float(df['col_91']) + float(df['col_92']) + float(df['col_93']) + float(df['col_94']) + float(df['col_95']) + float(df['col_96']) + float(df['col_99']) + float(df['col_100']) + float(df['col_101']) + float(df['col_102']) + float(df['col_103']) + float(df['col_104']) + float(df['col_106']) + float(df['col_107']) + float(df['col_108']) + float(df['col_109']) + float(df['col_110'])):
                return 'Inconsistent'
        elif float(df['col_112']) > float(df['col_73']) + float(df['col_74']) + float(df['col_75']) + float(df['col_76']) + float(df['col_77']) + float(df['col_78']) + float(df['col_79']) + float(df['col_80']) + float(df['col_85']) + float(df['col_86']) + float(df['col_87']) + float(df['col_88']) + float(df['col_89']) + float(df['col_90']) + float(df['col_91']) + float(df['col_92']) + float(df['col_93']) + float(df['col_94']) + float(df['col_95']) + float(df['col_96']) + float(df['col_99']) + float(df['col_100']) + float(df['col_101']) + float(df['col_102']) + float(df['col_103']) + float(df['col_104']) + float(df['col_106']) + float(df['col_107']) + float(df['col_108']) + float(df['col_109']) + float(df['col_110']):
            return 'Inconsistent (check fails)'
        else:
            return 'consistent'
        return df

    # 6.6.2<=6.1.1+6.1.2+6.1.3+6.1.4+6.1.5+6.1.6+6.1.7+6.1.8+6.1.13+6.1.14+6.1.15+6.1.16+6.1.17+6.1.18+6.1.19+6.1.20+6.1.21+6.2.1+6.2.2+6.2.3+6.3.1+6.3.2+6.3.3+6.4.1+6.4.2+6.4.3+6.4.5+6.4.6+6.5.1+6.5.2+6.5.3+6.5.4
    def res23(df):

        if pd.isnull(df['col_113']) and pd.isnull(df['col_73']) and pd.isnull(df['col_74']) and pd.isnull(df['col_75']) and pd.isnull(df['col_76']) and pd.isnull(df['col_77']) and pd.isnull(df['col_78']) and pd.isnull(df['col_79']) and pd.isnull(df['col_80']) and pd.isnull(df['col_85']) and pd.isnull(df['col_86']) and pd.isnull(df['col_87']) and pd.isnull(df['col_88']) and pd.isnull(df['col_89']) and pd.isnull(df['col_90']) and pd.isnull(df['col_91']) and pd.isnull(df['col_92']) and pd.isnull(df['col_93']) and pd.isnull(df['col_94']) and pd.isnull(df['col_95']) and pd.isnull(df['col_96']) and pd.isnull(df['col_99']) and pd.isnull(df['col_100']) and pd.isnull(df['col_101']) and pd.isnull(df['col_102']) and pd.isnull(df['col_103']) and pd.isnull(df['col_104']) and pd.isnull(df['col_106']) and pd.isnull(df['col_107']) and pd.isnull(df['col_108']) and pd.isnull(df['col_109']) and pd.isnull(df['col_110']):
            return 'Blank'
        elif pd.isnull(df['col_113']) or pd.isnull(df['col_73']) or pd.isnull(df['col_74']) or pd.isnull(df['col_75']) or pd.isnull(df['col_76']) or pd.isnull(df['col_77']) or pd.isnull(df['col_78']) or pd.isnull(df['col_79']) or pd.isnull(df['col_80']) or pd.isnull(df['col_85']) or pd.isnull(df['col_86']) or pd.isnull(df['col_87']) or pd.isnull(df['col_88']) or pd.isnull(df['col_89']) or pd.isnull(df['col_90']) or pd.isnull(df['col_91']) or pd.isnull(df['col_92']) or pd.isnull(df['col_93']) or pd.isnull(df['col_122']) or pd.isnull(df['col_94']) or pd.isnull(df['col_96']) or pd.isnull(df['col_99']) or pd.isnull(df['col_100']) or pd.isnull(df['col_101']) or pd.isnull(df['col_102']) or pd.isnull(df['col_103']) or pd.isnull(df['col_104']) or pd.isnull(df['col_106']) or pd.isnull(df['col_107']) or pd.isnull(df['col_108']) or pd.isnull(df['col_109']) or pd.isnull(df['col_110']):
            if pd.isnull(df['col_113']):
                return 'Probable Reporting Error (6.6.2 is blank)'
            elif pd.isnull(float(df['col_73']) + float(df['col_74']) + float(df['col_75']) + float(df['col_76']) + float(df['col_77']) + float(df['col_78']) + float(df['col_79']) + float(df['col_80']) + float(df['col_85']) + float(df['col_86']) + float(df['col_87']) + float(df['col_88']) + float(df['col_89']) + float(df['col_90']) + float(df['col_91']) + float(df['col_92']) + float(df['col_93']) + float(df['col_94']) + float(df['col_95']) + float(df['col_96']) + float(df['col_99']) + float(df['col_100']) + float(df['col_101']) + float(df['col_102']) + float(df['col_103']) + float(df['col_104']) + float(df['col_106']) + float(df['col_107']) + float(df['col_108']) + float(df['col_109']) + float(df['col_110'])):
                return 'Inconsistent'
        elif float(df['col_113']) > float(df['col_73']) + float(df['col_74']) + float(df['col_75']) + float(df['col_76']) + float(df['col_77']) + float(df['col_78']) + float(df['col_79']) + float(df['col_80']) + float(df['col_85']) + float(df['col_86']) + float(df['col_87']) + float(df['col_88']) + float(df['col_89']) + float(df['col_90']) + float(df['col_91']) + float(df['col_92']) + float(df['col_93']) + float(df['col_94']) + float(df['col_95']) + float(df['col_96']) + float(df['col_99']) + float(df['col_100']) + float(df['col_101']) + float(df['col_102']) + float(df['col_103']) + float(df['col_104']) + float(df['col_106']) + float(df['col_107']) + float(df['col_108']) + float(df['col_109']) + float(df['col_110']):
            return 'Inconsistent (check fails)'
        else:
            return 'consistent'
        return df

        # 6.6.3<=6.1.1+6.1.2+6.1.3+6.1.4+6.1.5+6.1.6+6.1.7+6.1.8+6.1.13+6.1.14+6.1.15+6.1.16+6.1.17+6.1.18+6.1.19+6.1.20+6.1.21+6.2.1+6.2.2+6.2.3+6.3.1+6.3.2+6.3.3+6.4.1+6.4.2+6.4.3+6.4.5+6.4.6+6.5.1+6.5.2+6.5.3+6.5.4
    def res24(df):

        if pd.isnull(df['col_114']) and pd.isnull(df['col_73']) and pd.isnull(df['col_74']) and pd.isnull(df['col_75']) and pd.isnull(df['col_76']) and pd.isnull(df['col_77']) and pd.isnull(df['col_78']) and pd.isnull(df['col_79']) and pd.isnull(df['col_80']) and pd.isnull(df['col_85']) and pd.isnull(df['col_86']) and pd.isnull(df['col_87']) and pd.isnull(df['col_88']) and pd.isnull(df['col_89']) and pd.isnull(df['col_90']) and pd.isnull(df['col_91']) and pd.isnull(df['col_92']) and pd.isnull(df['col_93']) and pd.isnull(df['col_94']) and pd.isnull(df['col_95']) and pd.isnull(df['col_96']) and pd.isnull(df['col_99']) and pd.isnull(df['col_100']) and pd.isnull(df['col_101']) and pd.isnull(df['col_102']) and pd.isnull(df['col_103']) and pd.isnull(df['col_104']) and pd.isnull(df['col_106']) and pd.isnull(df['col_107']) and pd.isnull(df['col_108']) and pd.isnull(df['col_109']) and pd.isnull(df['col_110']):
            return 'Blank'
        elif pd.isnull(df['col_114']) or pd.isnull(df['col_73']) or pd.isnull(df['col_74']) or pd.isnull(df['col_75']) or pd.isnull(df['col_76']) or pd.isnull(df['col_77']) or pd.isnull(df['col_78']) or pd.isnull(df['col_79']) or pd.isnull(df['col_80']) or pd.isnull(df['col_85']) or pd.isnull(df['col_86']) or pd.isnull(df['col_87']) or pd.isnull(df['col_88']) or pd.isnull(df['col_89']) or pd.isnull(df['col_90']) or pd.isnull(df['col_91']) or pd.isnull(df['col_92']) or pd.isnull(df['col_93']) or pd.isnull(df['col_122']) or pd.isnull(df['col_94']) or pd.isnull(df['col_96']) or pd.isnull(df['col_99']) or pd.isnull(df['col_100']) or pd.isnull(df['col_101']) or pd.isnull(df['col_102']) or pd.isnull(df['col_103']) or pd.isnull(df['col_104']) or pd.isnull(df['col_106']) or pd.isnull(df['col_107']) or pd.isnull(df['col_108']) or pd.isnull(df['col_109']) or pd.isnull(df['col_110']):
            if pd.isnull(df['col_114']):
                return 'Probable Reporting Error (6.6.1 is blank)'
            elif pd.isnull(float(df['col_73']) + float(df['col_74']) + float(df['col_75']) + float(df['col_76']) + float(df['col_77']) + float(df['col_78']) + float(df['col_79']) + float(df['col_80']) + float(df['col_85']) + float(df['col_86']) + float(df['col_87']) + float(df['col_88']) + float(df['col_89']) + float(df['col_90']) + float(df['col_91']) + float(df['col_92']) + float(df['col_93']) + float(df['col_94']) + float(df['col_95']) + float(df['col_96']) + float(df['col_99']) + float(df['col_100']) + float(df['col_101']) + float(df['col_102']) + float(df['col_103']) + float(df['col_104']) + float(df['col_106']) + float(df['col_107']) + float(df['col_108']) + float(df['col_109']) + float(df['col_110'])):
                return 'Inconsistent'
        elif float(df['col_114']) > float(df['col_73']) + float(df['col_74']) + float(df['col_75']) + float(df['col_76']) + float(df['col_77']) + float(df['col_78']) + float(df['col_79']) + float(df['col_80']) + float(df['col_85']) + float(df['col_86']) + float(df['col_87']) + float(df['col_88']) + float(df['col_89']) + float(df['col_90']) + float(df['col_91']) + float(df['col_92']) + float(df['col_93']) + float(df['col_94']) + float(df['col_95']) + float(df['col_96']) + float(df['col_99']) + float(df['col_100']) + float(df['col_101']) + float(df['col_102']) + float(df['col_103']) + float(df['col_104']) + float(df['col_106']) + float(df['col_107']) + float(df['col_108']) + float(df['col_109']) + float(df['col_110']):
            return 'Inconsistent (check fails)'
        else:
            return 'consistent'
        return df

    # 6.7.3<=6.7.2
    def res25(df):

        if pd.isnull(df['col_117']) and pd.isnull(df['col_116']):
            return 'Blank'
        elif pd.isnull(df['col_117']) or pd.isnull(df['col_116']):
            if pd.isnull(df['col_117']):
                return 'Probable Reporting Error (6.7.3 is blank)'
        elif pd.isnull(df['col_116']):
            return 'Inconsistent (6.7.2 is blank)'
        elif float(df['col_117']) > float(df['col_116']):
            return 'Inconsistent (check fails)'
        else:
            return 'consistent'
        return df

    # 10.1.2<=10.1.1
    def res26(df):
        if pd.isnull(df['col_144']) and pd.isnull(df['col_143']):
            return 'Blank'
        elif pd.isnull(df['col_144']) or pd.isnull(df['col_143']):
            if pd.isnull(df['col_144']):
                return 'Probable Reporting Error (10.1.2 is blank)'
            elif pd.isnull(df['col_143']):
                return 'Inconsistent (10.1.1 is blank)'
        elif float(df['col_144']) > float(df['col_143']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 10.2.1.b<=10.2.1.a
    def res27(df):

        if pd.isnull(df['col_146']) and pd.isnull(df['col_145']):
            return 'Blank'
        elif pd.isnull(df['col_146']) or pd.isnull(df['col_145']):
            if pd.isnull(df['col_146']):
                return 'Probable Reporting Error (10.2.1.b is blank)'
            elif pd.isnull(df['col_145']):
                return 'Inconsistent (10.2.1.a is blank)'
        elif float(df['col_146']) > float(df['col_145']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 3.1.1.a+3.1.1.b+3.1.3 >= 2.1.1.a+2.1.1.b+2.2
    def res28(df):

        if pd.isnull(df['col_46']) and pd.isnull(df['col_47']) and pd.isnull(df['col_49']) and pd.isnull(df['col_39']) and pd.isnull(df['col_40']) and pd.isnull(df['col_43']):
            return 'Blank'
        elif pd.isnull(df['col_46']) or pd.isnull(df['col_47']) or pd.isnull(df['col_49']) or pd.isnull(df['col_39']) or pd.isnull(df['col_40']) or pd.isnull(df['col_43']):
            if pd.isnull(df['col_46']):
                return 'Inconsistent  (3.1.1.a is blank)'
            elif pd.isnull(df['col_47']):
                return 'Inconsistent (3.1.1.b is blank)'
            elif pd.isnull(df['col_49']):
                return 'Inconsistent (3.1.3 is blank)'
            elif pd.isnull(float(df['col_39']) + float(df['col_40']) + float(df['col_43'])):
                return 'Probable Reporting Error'
        elif float(df['col_46']) + float(df['col_47']) + float(df['col_49']) < float(df['col_39']) + float(df['col_40']) + float(df['col_43']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 8.1.1.c<=8.1.1.a
    def res29(df):

        if pd.isnull(df['col_131']) and pd.isnull(df['col_129']):
            return 'Blank'
        elif pd.isnull(df['col_131']) or pd.isnull(df['col_129']):
            if pd.isnull(df['col_131']):
                return 'Probable Reporting Error (8.1.1.c is blank)'
            elif pd.isnull(df['col_129']):
                return 'Inconsistent (8.1.1.a is blank)'
        elif float(df['col_131']) > float(df['col_129']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 9.2.1 + 9.2.2>= 9.1.1+ 9.1.2+ 9.1.3+ 9.1.4+ 9.1.5+ 9.1.6+ 9.1.7+ 9.1.8
    def res30(df):

        if pd.isnull(df['col_140']) and pd.isnull(df['col_141']) and pd.isnull(df['col_132']) and pd.isnull(df['col_133']) and pd.isnull(df['col_134']) and pd.isnull(df['col_135']) and pd.isnull(df['col_136']) and pd.isnull(df['col_137']) and pd.isnull(df['col_138']) and pd.isnull(df['col_139']):
            return 'Blank'
        elif pd.isnull(df['col_140']) or pd.isnull(df['col_141']) or pd.isnull(df['col_132']) or pd.isnull(df['col_133']) or pd.isnull(df['col_134']) or pd.isnull(df['col_135']) or pd.isnull(df['col_136']) or pd.isnull(df['col_137']) or pd.isnull(df['col_138']) or pd.isnull(df['col_139']):
            if pd.isnull(float(df['col_140']) + float(df['col_141'])):
                return 'Inconsistent'
            # elif pd.isnull(df['col_141']):
            #     return 'Inconsistent (9.2.2 is blank)'
            elif pd.isnull(float(df['col_132']) + float(df['col_133']) + float(df['col_134']) + float(df['col_135']) + float(df['col_136']) + float(df['col_137']) + float(df['col_138']) + float(df['col_139'])):
                return 'Probable Reporting Error'
        elif float(df['col_140']) + float(df['col_141']) < float(df['col_132']) + float(df['col_133']) + float(df['col_134']) + float(df['col_135']) + float(df['col_136']) + float(df['col_137']) + float(df['col_138']) + float(df['col_139']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 8.1.1.b<=8.1.1.a
    def res31(df):

        if pd.isnull(df['col_130']) and pd.isnull(df['col_129']):
            return 'Blank'
        elif pd.isnull(df['col_130']) or pd.isnull(df['col_129']):
            if pd.isnull(df['col_130']):
                return 'Probable Reporting Error (8.1.1.b is blank)'
            elif pd.isnull(df['col_129']):
                return 'Inconsistent (8.1.1.a is blank)'
        elif float(df['col_130']) > float(df['col_129']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # Renaming column names
    # =====================
    df['4.3 <= 2.1.1.a + 2.1.1.b + 2.2'] = df.apply(res1, axis=1)
    df['1.1 <= 1.1.1'] = df.apply(res2, axis=1)
    df['1.3.1.a <= 1.3.1'] = df.apply(res3, axis=1)
    df['1.2.7 <= 1.1'] = df.apply(res4, axis=1)
    df['1.5.1.a <= 1.1'] = df.apply(res5, axis=1)
    df['1.5.1.b <= 1.5.1.a'] = df.apply(res6, axis=1)
    df['2.1.2 <= 2.1.1.a + 2.1.1.b'] = df.apply(res7, axis=1)
    df['2.1.3 <= 2.1.1.a + 2.1.1.b'] = df.apply(res8, axis=1)
    df['2.2.2 <= 2.2'] = df.apply(res9, axis=1)
    df['4.4 <= 2.1.1.a + 2.1.1.b + 2.2'] = df.apply(res10, axis=1)
    df['6.1.1 <= 3.1.1.a + 3.1.1.b'] = df.apply(res11, axis=1)
    df['6.1.9 <= 3.1.1.a + 3.1.1.b'] = df.apply(res12, axis=1)
    df['6.1.13 <= 3.1.1.a + 3.1.1.b'] = df.apply(res13, axis=1)
    df['2.2.1 <= 2.2'] = df.apply(res14, axis=1)
    df['3.1.2 <= 3.1.1.a + 3.1.1.b'] = df.apply(res15, axis=1)
    df['3.3.1 <= 3.1.1.a + 3.1.1.b'] = df.apply(res16, axis=1)
    df['3.3.2 <= 3.3.1'] = df.apply(res17, axis=1)
    df['3.3.3 <= 3.1.1.a + 3.1.1.b'] = df.apply(res18, axis=1)
    df['4.1 <= 2.1.1.a + 2.1.1.b'] = df.apply(res19, axis=1)
    df['5.2 <= 2.1.1.a + 2.1.1.b + 2.2'] = df.apply(res20, axis=1)
    df['6.2.4.a + 6.2.4.b <= 6.2.1 + 6.2.2'] = df.apply(res21, axis=1)
    df['6.6.1<=6.1.1+6.1.2+6.1.3+6.1.4+6.1.5+6.1.6+6.1.7+6.1.8+6.1.13+6.1.14+6.1.15+6.1.16+6.1.17+6.1.18+6.1.19+6.1.20+6.1.21+6.2.1+6.2.2+6.2.3+6.3.1+6.3.2+6.3.3+6.4.1+6.4.2+6.4.3+6.4.5+6.4.6+6.5.1+6.5.2+6.5.3+6.5.4'] = df.apply(res22, axis=1)
    df['6.6.2<=6.1.1+6.1.2+6.1.3+6.1.4+6.1.5+6.1.6+6.1.7+6.1.8+6.1.13+6.1.14+6.1.15+6.1.16+6.1.17+6.1.18+6.1.19+6.1.20+6.1.21+6.2.1+6.2.2+6.2.3+6.3.1+6.3.2+6.3.3+6.4.1+6.4.2+6.4.3+6.4.5+6.4.6+6.5.1+6.5.2+6.5.3+6.5.4'] = df.apply(res23, axis=1)
    df['6.6.3<=6.1.1+6.1.2+6.1.3+6.1.4+6.1.5+6.1.6+6.1.7+6.1.8+6.1.13+6.1.14+6.1.15+6.1.16+6.1.17+6.1.18+6.1.19+6.1.20+6.1.21+6.2.1+6.2.2+6.2.3+6.3.1+6.3.2+6.3.3+6.4.1+6.4.2+6.4.3+6.4.5+6.4.6+6.5.1+6.5.2+6.5.3+6.5.4'] = df.apply(res24, axis=1)
    df['6.7.3<=6.7.2'] = df.apply(res25, axis=1)
    df['10.1.2<=10.1.1'] = df.apply(res26, axis=1)
    df['10.2.1.b<=10.2.1.a'] = df.apply(res27, axis=1)
    df['3.1.1.a+3.1.1.b+3.1.3 >= 2.1.1.a+2.1.1.b+2.2'] = df.apply(res28, axis=1)
    df['8.1.1.c<=8.1.1.a'] = df.apply(res29, axis=1)
    df['9.2.1 + 9.2.2>= 9.1.1+ 9.1.2+ 9.1.3+ 9.1.4+ 9.1.5+ 9.1.6+ 9.1.7+ 9.1.8'] = df.apply(res30, axis=1)
    df['8.1.1.b<=8.1.1.a'] = df.apply(res31, axis=1)

    # Merging all the renamed columns
    # ===============================
    df = pd.concat([df['4.3 <= 2.1.1.a + 2.1.1.b + 2.2'],
                    df['1.1 <= 1.1.1'],
                    df['1.3.1.a <= 1.3.1'],
                    df['1.2.7 <= 1.1'],
                    df['1.5.1.a <= 1.1'],
                    df['1.5.1.b <= 1.5.1.a'],
                    df['2.1.2 <= 2.1.1.a + 2.1.1.b'],
                        df['2.1.3 <= 2.1.1.a + 2.1.1.b'],
                        df['2.2.2 <= 2.2'],
                        df['4.4 <= 2.1.1.a + 2.1.1.b + 2.2'],
                        df['6.1.1 <= 3.1.1.a + 3.1.1.b'],
                        df['6.1.9 <= 3.1.1.a + 3.1.1.b'],
                        df['6.1.13 <= 3.1.1.a + 3.1.1.b'],
                        df['2.2.1 <= 2.2'],
                        df['3.1.2 <= 3.1.1.a + 3.1.1.b'],
                        df['3.3.1 <= 3.1.1.a + 3.1.1.b'],
                            df['3.3.2 <= 3.3.1'],
                            df['3.3.3 <= 3.1.1.a + 3.1.1.b'],
                            df['4.1 <= 2.1.1.a + 2.1.1.b'],
                            df['5.2 <= 2.1.1.a + 2.1.1.b + 2.2'],
                            df['6.2.4.a + 6.2.4.b <= 6.2.1 + 6.2.2'],
                            df['6.6.1<=6.1.1+6.1.2+6.1.3+6.1.4+6.1.5+6.1.6+6.1.7+6.1.8+6.1.13+6.1.14+6.1.15+6.1.16+6.1.17+6.1.18+6.1.19+6.1.20+6.1.21+6.2.1+6.2.2+6.2.3+6.3.1+6.3.2+6.3.3+6.4.1+6.4.2+6.4.3+6.4.5+6.4.6+6.5.1+6.5.2+6.5.3+6.5.4'],
                            df['6.6.2<=6.1.1+6.1.2+6.1.3+6.1.4+6.1.5+6.1.6+6.1.7+6.1.8+6.1.13+6.1.14+6.1.15+6.1.16+6.1.17+6.1.18+6.1.19+6.1.20+6.1.21+6.2.1+6.2.2+6.2.3+6.3.1+6.3.2+6.3.3+6.4.1+6.4.2+6.4.3+6.4.5+6.4.6+6.5.1+6.5.2+6.5.3+6.5.4'],
                            df['6.6.3<=6.1.1+6.1.2+6.1.3+6.1.4+6.1.5+6.1.6+6.1.7+6.1.8+6.1.13+6.1.14+6.1.15+6.1.16+6.1.17+6.1.18+6.1.19+6.1.20+6.1.21+6.2.1+6.2.2+6.2.3+6.3.1+6.3.2+6.3.3+6.4.1+6.4.2+6.4.3+6.4.5+6.4.6+6.5.1+6.5.2+6.5.3+6.5.4'],
                            df['6.7.3<=6.7.2'],
                            df['10.1.2<=10.1.1'],
                                df['10.2.1.b<=10.2.1.a'],
                                df['3.1.1.a+3.1.1.b+3.1.3 >= 2.1.1.a+2.1.1.b+2.2'],
                                df['8.1.1.c<=8.1.1.a'],
                                df['9.2.1 + 9.2.2>= 9.1.1+ 9.1.2+ 9.1.3+ 9.1.4+ 9.1.5+ 9.1.6+ 9.1.7+ 9.1.8'],
                                df['8.1.1.b<=8.1.1.a']], axis=1)



    # Mergining current result of modified checks with original dataframe and displaying it on screen
    frames = [df_, df]
    print(frames)
    df = pd.concat(frames, axis=1, sort=False)


    # Create the messagebox object
    self.msg = QMessageBox()
    # Set the information icon
    self.msg.setWindowIcon(QtGui.QIcon('checked.png'))
    self.msg.setStyleSheet("QLabel {border: 2px solid green; margin-right: 15px ; font-size: 18px; font-family: Arial;} QPushButton {background-color:lightgreen; font-family: Arial; font-size:20px;} ")
    # Set the main message
    self.msg.setText("Health Sub Centre validation successfully complete.")
    # Set the title of the window
    self.msg.setWindowTitle("Validation Successful Message")
    # Display the message box
    self.msg.show()

    return df

# To reference df
def load_HSC(self):
    return df
