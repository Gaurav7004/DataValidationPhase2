import pandas as pd
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox

#############################################################################################
# Public Health Center Validation Rules Function
def PHC_Validate(self, df_):
    global df

    df = self.loadFile(df_)

    filterString = self.lineEdit_2.text()
    
    df = df_.loc[df_['col_12'] == filterString]
    print(df)
    #df = df.dropna(subset=['col_18', 'col_19'], inplace=True)
    print('Entered PHC_Validate')

    # Modified Checks of PHC
    
    # 9.1.1(103) <= 4.1.1.a(56) + 4.1.1.b(57)
    def res1(df):
        if pd.isnull(df['col_103']) and pd.isnull(df['col_56']) and pd.isnull(df['col_57']):
            return 'Blank'
        elif pd.isnull(df['col_103']) or pd.isnull(df['col_56']) or pd.isnull(df['col_57']):
            if pd.isnull(df['col_59']):
                return 'Probable Reporting Error(9.1.1 is blank)'
            elif pd.isnull(float(df['col_56']) + float(df['col_57'])):
                return 'Inconsistent'
        elif float(df['col_103']) > float(df['col_56']) + float(df['col_57']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 1.1.1(23) <= 1.1(22)
    def res2(df):
        if pd.isnull(df['col_23']) and pd.isnull(df['col_22']):
            return 'Blank'
        elif pd.isnull(df['col_23']) or pd.isnull(df['col_22']):
            if pd.isnull(df['col_23']):
                return 'Probable Reporting Error(1.1.1 is blank)'
            elif pd.isnull(df['col_22']):
                return 'Inconsistent'
        elif float(df['col_23']) > float(df['col_22']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 1.2.4(27) <= 1.1(22)
    def res3(df):
        if pd.isnull(df['col_27']) and pd.isnull(df['col_22']):
            return 'Blank'
        elif pd.isnull(df['col_27']) or pd.isnull(df['col_22']):
            if pd.isnull(df['col_27']) and not pd.isnull(float(df['col_22'])):
                return 'Probable Reporting Error'
            else:
                return 'Probable Reporting Error'

        # If value exists for all the elements
        else:

            lhs_value = float(df['col_27'])
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

    # 1.2.5(28) <= 1.1(22)
    def res4(df):
        if pd.isnull(df['col_28']) and pd.isnull(df['col_22']):
            return 'Blank'
        elif pd.isnull(df['col_28']) or pd.isnull(df['col_22']):
            if pd.isnull(df['col_28']) and not pd.isnull(float(df['col_22'])):
                return 'Probable Reporting Error'
            else:
                return 'Probable Reporting Error'

        # If value exists for all the elements
        else:

            lhs_value = float(df['col_28'])
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

    # 1.2.7(30) <= 1.1(22)
    def res5(df):
        if pd.isnull(df['col_30']) and pd.isnull(df['col_22']):
            return 'Blank'
        elif pd.isnull(df['col_30']) or pd.isnull(df['col_22']):
            if pd.isnull(df['col_30']) and not pd.isnull(float(df['col_22'])):
                return 'Probable Reporting Error'
            else:
                return 'Probable Reporting Error'

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

    # 2.1.2(49) <= 2.1.1.a(47) + 2.1.1.b(48)
    def res6(df):
        if pd.isnull(df['col_49']) and pd.isnull(df['col_47']) and pd.isnull(df['col_48']):
            return 'Blank'
        elif pd.isnull(df['col_49']) or pd.isnull(df['col_47']) or pd.isnull(df['col_48']):
            if pd.isnull(df['col_49']):
                return 'Probable Reporting Error(2.1.2 is blank)'
            elif pd.isnull(float(df['col_47']) + float(df['col_48'])):
                return 'Inconsistent'
        elif float(df['col_49']) > float(df['col_47']) + float(df['col_48']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 2.1.3(50) <= 2.1.1.a(47) + 2.1.1.b(48)
    def res7(df):
        if pd.isnull(df['col_50']) and pd.isnull(df['col_47']) and pd.isnull(df['col_48']):
            return 'Blank'
        elif pd.isnull(df['col_50']) or pd.isnull(df['col_47']) or pd.isnull(df['col_48']):
            if pd.isnull(df['col_50']) and not pd.isnull(float(df['col_47'])) and pd.isnull(float(df['col_48'])):
                return 'Probable Reporting Error'
            else:
                return 'Probable Reporting Error'

        # If value exists for all the elements
        else:

            lhs_value = float(df['col_47'])
            rhs_value = float(df['col_48'])

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

    # 2.2.1(52) <= 2.2(51)
    def res8(df):
        if pd.isnull(df['col_52']) and pd.isnull(df['col_51']):
            return 'Blank'
        elif pd.isnull(df['col_52']) or pd.isnull(df['col_51']):
            if pd.isnull(df['col_52']):
                return 'Probable Reporting Error(2.2.1 is blank)'
            elif pd.isnull(df['col_56']):
                return 'Inconsistent'
        elif float(df['col_103']) > float(df['col_56']) + float(df['col_57']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 2.2(51) >= 1.3.2(34)
    def res9(df):
        if pd.isnull(df['col_51']) and pd.isnull(df['col_34']):
            return 'Blank'
        elif pd.isnull(df['col_51']) or pd.isnull(df['col_34']):
            if pd.isnull(df['col_51']):
                return 'Probable Reporting Error(2.2 is blank)'
            elif pd.isnull(df['col_34']):
                return 'Inconsistent'
        elif float(df['col_51']) < float(df['col_34']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 1.4.4(38) >= 1.4.3(37)
    def res10(df):
        if pd.isnull(df['col_38']) and pd.isnull(df['col_37']):
            return 'Blank'
        elif pd.isnull(df['col_38']) or pd.isnull(df['col_37']):
            if pd.isnull(df['col_38']) and not pd.isnull(float(df['col_37'])):
                return 'Probable Reporting Error'
            else:
                return 'Probable Reporting Error'

        # If value exists for all the elements
        else:

            lhs_value = float(df['col_38'])
            rhs_value = float(df['col_37'])

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

    # 1.5.1(39) <= 1.1(22)
    def res11(df):
        if pd.isnull(df['col_39']) and pd.isnull(df['col_22']):
            return 'Blank'
        elif pd.isnull(df['col_39']) or pd.isnull(df['col_22']):
            if pd.isnull(df['col_39']):
                return 'Probable Reporting Error(1.5.1 is blank)'
            elif pd.isnull(df['col_22']):
                return 'Inconsistent'
        elif float(df['col_39']) < float(df['col_22']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 1.5.2(40) <= 1.5.1(39)
    def res12(df):
        if pd.isnull(df['col_40']) and pd.isnull(df['col_39']):
            return 'Blank'
        elif pd.isnull(df['col_40']) or pd.isnull(df['col_39']):
            if pd.isnull(df['col_40']):
                return 'Probable Reporting Error(1.5.1 is blank)'
            elif pd.isnull(df['col_39']):
                return 'Inconsistent'
        elif float(df['col_40']) < float(df['col_39']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 1.5.3(41) <= 1.5.2(40)
    def res13(df):
        if pd.isnull(df['col_41']) and pd.isnull(df['col_40']):
            return 'Blank'
        elif pd.isnull(df['col_41']) or pd.isnull(df['col_40']):
            if pd.isnull(df['col_41']):
                return 'Probable Reporting Error(1.5.3 is blank)'
            elif pd.isnull(df['col_40']):
                return 'Inconsistent'
        elif float(df['col_41']) < float(df['col_40']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 1.6.1.a(42) <= 1.1(22)
    def res14(df):
        if pd.isnull(df['col_42']) and pd.isnull(df['col_22']):
            return 'Blank'
        elif pd.isnull(df['col_42']) or pd.isnull(df['col_22']):
            if pd.isnull(df['col_42']):
                return 'Probable Reporting Error(1.6.1.a is blank)'
            elif pd.isnull(df['col_22']):
                return 'Inconsistent'
        elif float(df['col_42']) < float(df['col_22']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 1.6.1.b(43) <= 1.6.1.a(42)
    def res15(df):
        if pd.isnull(df['col_43']) and pd.isnull(df['col_42']):
            return 'Blank'
        elif pd.isnull(df['col_43']) or pd.isnull(df['col_42']):
            if pd.isnull(df['col_43']):
                return 'Probable Reporting Error(1.6.1.a is blank)'
            elif pd.isnull(df['col_42']):
                return 'Inconsistent'
        elif float(df['col_43']) < float(df['col_42']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 1.6.1.c(44) <= 1.6.1.b(43)
    def res16(df):
        if pd.isnull(df['col_44']) and pd.isnull(df['col_43']):
            return 'Blank'
        elif pd.isnull(df['col_44']) or pd.isnull(df['col_43']):
            if pd.isnull(df['col_44']):
                return 'Probable Reporting Error(1.6.1.a is blank)'
            elif pd.isnull(df['col_43']):
                return 'Inconsistent'
        elif float(df['col_44']) > float(df['col_43']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 1.6.1.e(46) <= 1.6.1.d(45)
    def res17(df):
        if pd.isnull(df['col_46']) and pd.isnull(df['col_45']):
            return 'Blank'
        elif pd.isnull(df['col_46']) or pd.isnull(df['col_45']):
            if pd.isnull(df['col_46']):
                return 'Probable Reporting Error(1.6.1.e is blank)'
            elif pd.isnull(df['col_45']):
                return 'Inconsistent'
        elif float(df['col_46']) > float(df['col_45']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 3.1.1(55) <= 2.2(51)
    def res18(df):
        if pd.isnull(df['col_55']) and pd.isnull(df['col_51']):
            return 'Blank'
        elif pd.isnull(df['col_55']) or pd.isnull(df['col_51']):
            if pd.isnull(df['col_55']):
                return 'Probable Reporting Error(3.1.1 is blank)'
            elif pd.isnull(df['col_51']):
                return 'Inconsistent'
        elif float(df['col_55']) < float(df['col_51']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 3.1(54) <= 2.2(51)
    def res19(df):
        if pd.isnull(df['col_54']) and pd.isnull(df['col_51']):
            return 'Blank'
        elif pd.isnull(df['col_54']) or pd.isnull(df['col_51']):
            if pd.isnull(df['col_54']):
                return 'Probable Reporting Error(1.6.1.a is blank)'
            elif pd.isnull(df['col_51']):
                return 'Inconsistent'
        elif float(df['col_54']) < float(df['col_51']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 4.1.2(58) <= 4.1.1.a(56) + 4.1.1.b(57)
    def res20(df):
        if pd.isnull(df['col_58']) and pd.isnull(df['col_56']) and pd.isnull(df['col_57']):
            return 'Blank'
        elif pd.isnull(df['col_58']) or pd.isnull(df['col_56']) or pd.isnull(df['col_57']):
            if pd.isnull(df['col_58']):
                return 'Probable Reporting Error(4.1.2 is blank)'
            elif pd.isnull(float(df['col_56']) + float(df['col_57'])):
                return 'Inconsistent'
        elif float(df['col_58']) > float(df['col_56']) + float(df['col_57']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 4.1.1.a(56) + 4.1.1.b(57) + 4.1.3(59) >= 2.1.1.a(47) + 2.1.1.b(48) + 2.2(51)
    def res21(df):
        if pd.isnull(df['col_56']) and pd.isnull(df['col_57']) and pd.isnull(df['col_59']) and pd.isnull(df['col_47']) and pd.isnull(df['col_48']) and pd.isnull(df['col_51']):
            return 'Blank'
        elif pd.isnull(df['col_56']) or pd.isnull(df['col_57']) or pd.isnull(df['col_59']) or pd.isnull(df['col_47']) or pd.isnull(df['col_48']) or pd.isnull(df['col_51']):
            if pd.isnull(df['col_56']) + pd.isnull(df['col_57']) + pd.isnull(df['col_59']):
                return 'Inconsistent'
            elif pd.isnull(float(df['col_47']) + float(df['col_48']) + float(df['col_51'])):
                return 'Probable Reporting Error'
        elif float(df['col_56']) + float(df['col_57']) + float(df['col_59']) <  float(df['col_47']) + float(df['col_48']) + float(df['col_51']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 4.3.2.a(63) <= 4.3.1.a(61) + 4.3.1.b(62) + 4.2(60)
    def res22(df):
        if pd.isnull(df['col_63']) and pd.isnull(df['col_61']) and pd.isnull(df['col_62']) and pd.isnull(df['col_60']):
            return 'Blank'
        elif pd.isnull(df['col_63']) or pd.isnull(df['col_61']) or pd.isnull(df['col_62']) or pd.isnull(df['col_60']):
            if pd.isnull(df['col_63']):
                return 'Probable Reporting Error'
            elif pd.isnull((float(df['col_61']) + float(df['col_62']) + float(df['col_60']))):
                return 'Inconsistent'
        elif float(df['col_63']) > float(df['col_61']) + float(df['col_62']) + float(df['col_60']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 4.3.2.b(64) <= 4.3.2.a(63)
    def res23(df):
        if pd.isnull(df['col_64']) and pd.isnull(df['col_63']):
            return 'Blank'
        elif pd.isnull(df['col_64']) or pd.isnull(df['col_63']):
            if pd.isnull(df['col_64']):
                return 'Probable Reporting Error'
            elif pd.isnull(df['col_63']):
                return 'Inconsistent'
        elif float(df['col_64']) > float(df['col_63']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 4.3.3(65) <= 4.3.1.a(61) + 4.3.1.b(62) + 4.2(60)
    def res24(df):
        if pd.isnull(df['col_65']) and pd.isnull(df['col_61']) and pd.isnull(df['col_62']) and pd.isnull(df['col_60']):
            return 'Blank'
        elif pd.isnull(df['col_65']) or pd.isnull(df['col_61']) or pd.isnull(df['col_62']) or pd.isnull(df['col_60']):
            if pd.isnull(df['col_65']):
                return 'Probable Reporting Error'
            elif pd.isnull((float(df['col_61']) + float(df['col_62']) + float(df['col_60']))):
                return 'Inconsistent'
        elif float(df['col_65']) > float(df['col_61']) + float(df['col_62']) + float(df['col_60']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 4.4.1(66) <= 4.1.1.a(56) + 4.1.1.b(57)
    def res25(df):
        if pd.isnull(df['col_66']) and pd.isnull(df['col_56']) and pd.isnull(df['col_57']):
            return 'Blank'
        elif pd.isnull(df['col_66']) or pd.isnull(df['col_56']) or pd.isnull(df['col_57']):
            if pd.isnull(df['col_66']):
                return 'Probable Reporting Error'
            elif pd.isnull((float(df['col_56']) + float(df['col_57']))):
                return 'Inconsistent'
        elif float(df['col_66']) > float(df['col_56']) + float(df['col_57']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 4.4.2(67) <= 4.4.1(66)
    def res26(df):
        if pd.isnull(df['col_67']) and pd.isnull(df['col_66']):
            return 'Blank'
        elif pd.isnull(df['col_67']) or pd.isnull(df['col_66']):
            if pd.isnull(df['col_67']):
                return 'Probable Reporting Error'
            elif pd.isnull(df['col_66']):
                return 'Inconsistent'
        elif float(df['col_67']) > float(df['col_66']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 4.4.3(68) <= 4.1.1.a(56) + 4.1.1.b(57)
    def res27(df):
        if pd.isnull(df['col_68']) and pd.isnull(df['col_56']) and pd.isnull(df['col_57']):
            return 'Blank'
        elif pd.isnull(df['col_68']) or pd.isnull(df['col_56']) or pd.isnull(df['col_57']):
            if pd.isnull(df['col_68']):
                return 'Probable Reporting Error'
            elif pd.isnull((float(df['col_56']) + float(df['col_57']))):
                return 'Inconsistent'
        elif float(df['col_68']) > float(df['col_56']) + float(df['col_57']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 6.1(70) <= 2.1.1.a(47) + 2.1.1.b(48)
    def res28(df):
        if pd.isnull(df['col_70']) and pd.isnull(df['col_47']) and pd.isnull(df['col_48']):
            return 'Blank'
        elif pd.isnull(df['col_70']) or pd.isnull(df['col_47']) or pd.isnull(df['col_48']):
            if pd.isnull(df['col_70']):
                return 'Probable Reporting Error'
            elif pd.isnull((float(df['col_47'])) + (float(df['col_48']))):
                return 'Inconsistent'
        elif float(df['col_70']) > float(df['col_47']) + float(df['col_48']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 6.3(72) <= 2.1.1.a(47) + 2.1.1.b(48) + 2.2(51)
    def res29(df):
        if pd.isnull(df['col_72']) and pd.isnull(df['col_47']) and pd.isnull(df['col_48']) and pd.isnull(df['col_51']):
            return 'Blank'
        elif pd.isnull(df['col_72']) or pd.isnull(df['col_47']) or pd.isnull(df['col_48']) or pd.isnull(df['col_51']):
            if pd.isnull(df['col_72']) and not pd.isnull(float(df['col_47'])) and pd.isnull(float(df['col_48'])) and pd.isnull(float(df['col_51'])):
                return 'Probable Reporting Error'
            else:
                return 'Probable Reporting Error'

        # If value exists for all the elements
        else:

            lhs_value = float(df['col_72'])
            rhs_value = float(df['col_47']) + float(df['col_48']) + float(df['col_51']) 

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

    # 6.4(73) <= 2.1.1.a(47) + 2.1.1.b(48) + 2.2(51)
    def res30(df):
        if pd.isnull(df['col_73']) and pd.isnull(df['col_47']) and pd.isnull(df['col_48']) and pd.isnull(df['col_51']):
            return 'Blank'
        elif pd.isnull(df['col_73']) or pd.isnull(df['col_47']) or pd.isnull(df['col_48']) or pd.isnull(df['col_51']):
            if pd.isnull(df['col_73']) and not pd.isnull(float(df['col_47'])) and pd.isnull(float(df['col_48'])) and pd.isnull(float(df['col_51'])):
                return 'Probable Reporting Error'
            else:
                return 'Probable Reporting Error'

        # If value exists for all the elements
        else:

            lhs_value = float(df['col_73'])
            rhs_value = float(df['col_47']) + float(df['col_48']) + float(df['col_51']) 

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

    # 7.2.1(76) <= 7.1.1(74)
    def res31(df):
        if pd.isnull(df['col_76']) and pd.isnull(df['col_74']):
            return 'Blank'
        elif pd.isnull(df['col_76']) or pd.isnull(df['col_74']):
            if pd.isnull(df['col_76']):
                return 'Probable Reporting Error'
            elif pd.isnull(df['col_74']):
                return 'Inconsistent'
        elif float(df['col_76']) > float(df['col_74']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 7.2.2(77) <= 7.1.2(75)
    def res32(df):
        if pd.isnull(df['col_77']) and pd.isnull(df['col_75']):
            return 'Blank'
        elif pd.isnull(df['col_77']) or pd.isnull(df['col_75']):
            if pd.isnull(df['col_77']):
                return 'Probable Reporting Error'
            elif pd.isnull(df['col_75']):
                return 'Inconsistent'
        elif float(df['col_77']) > float(df['col_75']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 8.2.3(81) <= 2.2(51)
    def res33(df):
        if pd.isnull(df['col_81']) and pd.isnull(df['col_51']):
            return 'Blank'
        elif pd.isnull(df['col_81']) or pd.isnull(df['col_51']):
            if pd.isnull(df['col_81']):
                return 'Probable Reporting Error'
            elif pd.isnull(df['col_51']):
                return 'Inconsistent'
        elif float(df['col_81']) > float(df['col_51']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 8.4(84) <= 2.1.1.a(47) + 2.1.1.b(48) + 2.2(51)
    def res34(df):
        if pd.isnull(df['col_84']) and pd.isnull(df['col_61']) and pd.isnull(df['col_62']) and pd.isnull(df['col_60']):
            return 'Blank'
        elif pd.isnull(df['col_84']) or pd.isnull(df['col_61']) or pd.isnull(df['col_62']) or pd.isnull(df['col_60']):
            if pd.isnull(df['col_84']):
                return 'Probable Reporting Error'
            elif pd.isnull((float(df['col_61']) + float(df['col_62']) + float(df['col_60']))):
                return 'Inconsistent'
        elif float(df['col_84']) > float(df['col_61']) + float(df['col_62']) + float(df['col_60']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 8.7(87) <= 8.3(83) + 8.4(84) + 8.5(85)
    def res35(df):
        if pd.isnull(df['col_87']) and pd.isnull(df['col_83']) and pd.isnull(df['col_84']) and pd.isnull(df['col_85']):
            return 'Blank'
        elif pd.isnull(df['col_87']) or pd.isnull(df['col_83']) or pd.isnull(df['col_84']) or pd.isnull(df['col_85']):
            if pd.isnull(df['col_87']):
                return 'Probable Reporting Error'
            elif pd.isnull((float(df['col_83']) + float(df['col_84']) + float(df['col_85']))):
                return 'Inconsistent'
        elif float(df['col_87']) > float(df['col_83']) + float(df['col_84']) + float(df['col_85']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 8.17.1(97) <= 8.1.1(78)
    def res36(df):
        if pd.isnull(df['col_97']) and pd.isnull(df['col_78']):
            return 'Blank'
        elif pd.isnull(df['col_97']) or pd.isnull(df['col_78']):
            if pd.isnull(df['col_97']):
                return 'Probable Reporting Error'
            elif pd.isnull(df['col_78']):
                return 'Inconsistent'
        elif float(df['col_97']) > float(df['col_78']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 8.17.2(98) <= 8.2.1(79) + 8.2.2(80) + 8.2.3(81) + 8.2.4(82)
    def res37(df):
        if pd.isnull(df['col_98']) and pd.isnull(df['col_79']) and pd.isnull(df['col_80']) and pd.isnull(df['col_81']) and pd.isnull(df['col_82']):
            return 'Blank'
        elif pd.isnull(df['col_98']) or pd.isnull(df['col_79']) or pd.isnull(df['col_80']) or pd.isnull(df['col_81']) or pd.isnull(df['col_82']):
            if pd.isnull(df['col_98']):
                return 'Probable Reporting Error'
            elif pd.isnull((float(df['col_79']) + float(df['col_80']) + float(df['col_81']) + float(df['col_82']))):
                return 'Inconsistent'
        elif float(df['col_98']) > float(df['col_79']) + float(df['col_80']) + float(df['col_81']) + float(df['col_82']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 9.1.9(111) <= 4.1.1.a(56) + 4.1.1.b(57)
    def res38(df):
        if pd.isnull(df['col_111']) and pd.isnull(df['col_56']) and pd.isnull(df['col_57']):
            return 'Blank'
        elif pd.isnull(df['col_111']) or pd.isnull(df['col_56']) or pd.isnull(df['col_57']):
            if pd.isnull(df['col_111']):
                return 'Probable Reporting Error'
            elif pd.isnull(float(df['col_56']) + float(df['col_57'])):
                return 'Inconsistent'
        elif float(df['col_111']) > float(df['col_56']) + float(df['col_57']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 9.1.13(115) <= 4.1.1.a(56) + 4.1.1.b(57)
    def res39(df):
        if pd.isnull(df['col_115']) and pd.isnull(df['col_56']) and pd.isnull(df['col_57']):
            return 'Blank'
        elif pd.isnull(df['col_115']) or pd.isnull(df['col_56']) or pd.isnull(df['col_57']):
            if pd.isnull(df['col_115']):
                return 'Probable Reporting Error'
            elif pd.isnull(float(df['col_56']) + float(df['col_57'])):
                return 'Inconsistent'
        elif float(df['col_115']) > float(df['col_56']) + float(df['col_57']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 9.2.4.a(127) + 9.2.4.b(128) <= 9.2.1(124) + 9.2.2(125)
    def res40(df):
        if pd.isnull(df['col_127']) and pd.isnull(df['col_128']) and pd.isnull(df['col_124']) and pd.isnull(df['col_125']):
            return 'Blank'
        elif pd.isnull(df['col_127']) or pd.isnull(df['col_128']) or pd.isnull(df['col_124']) or pd.isnull(df['col_125']):
            if pd.isnull(float(df['col_127']) + float(df['col_128'])):
                return 'Probable Reporting Error'
            elif pd.isnull(float(df['col_124']) + float(df['col_125'])):
                return 'Inconsistent'
        elif float(df['col_127']) + float(df['col_128']) > float(df['col_124']) + float(df['col_125']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 11.2.2(175) <= 11.2.1(174)
    def res41(df):
        if pd.isnull(df['col_175']) and pd.isnull(df['col_174']):
            return 'Blank'
        elif pd.isnull(df['col_175']) or pd.isnull(df['col_174']):
            if pd.isnull(df['col_175']):
                return 'Probable Reporting Error'
            elif pd.isnull(df['col_174']):
                return 'Inconsistent'
        elif float(df['col_175']) > float(df['col_174']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 12.1.2.a(180) <= 12.1.1.a(178)
    def res42(df):
        if pd.isnull(df['col_180']) and pd.isnull(df['col_178']):
            return 'Blank'
        elif pd.isnull(df['col_180']) or pd.isnull(df['col_178']):
            if pd.isnull(df['col_180']):
                return 'Probable Reporting Error'
            elif pd.isnull(df['col_178']):
                return 'Inconsistent'
        elif float(df['col_180']) > float(df['col_178']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 12.1.2.b(181) <= 12.1.1.b(179)
    def res43(df):
        if pd.isnull(df['col_181']) and pd.isnull(df['col_179']):
            return 'Blank'
        elif pd.isnull(df['col_181']) or pd.isnull(df['col_179']):
            if pd.isnull(df['col_181']):
                return 'Probable Reporting Error'
            elif pd.isnull(df['col_179']):
                return 'Inconsistent'
        elif float(df['col_181']) > float(df['col_179']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 12.1.3.a(182) <= 12.1.1.a(178)
    def res44(df):
        if pd.isnull(df['col_182']) and pd.isnull(df['col_178']):
            return 'Blank'
        elif pd.isnull(df['col_182']) or pd.isnull(df['col_178']):
            if pd.isnull(df['col_182']):
                return 'Probable Reporting Error'
            elif pd.isnull(df['col_178']):
                return 'Inconsistent'
        elif float(df['col_182']) > float(df['col_178']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 12.1.3.b(183) <= 12.1.1.b(179)
    def res45(df):
        if pd.isnull(df['col_183']) and pd.isnull(df['col_179']):
            return 'Blank'
        elif pd.isnull(df['col_183']) or pd.isnull(df['col_179']):
            if pd.isnull(df['col_183']):
                return 'Probable Reporting Error'
            elif pd.isnull(df['col_179']):
                return 'Inconsistent'
        elif float(df['col_183']) > float(df['col_179']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 14.2.1(194) + 14.2.2(195) >= 14.1.1(186) + 14.1.2(187) + 14.1.3(188) + 14.1.4(189) + 14.1.5(190) + 14.1.6(191) + 14.1.7(192) + 14.1.8(193)
    def res46(df):
        if pd.isnull(df['col_194']) and pd.isnull(df['col_195']) and pd.isnull(df['col_186']) and pd.isnull(df['col_187']) and pd.isnull(df['col_188']) and pd.isnull(df['col_189']) and pd.isnull(df['col_190']) and pd.isnull(df['col_191']) and pd.isnull(df['col_192']) and pd.isnull(df['col_193']):
            return 'Blank'
        elif pd.isnull(df['col_194']) or pd.isnull(df['col_195']) or pd.isnull(df['col_186']) or pd.isnull(df['col_187']) or pd.isnull(df['col_188']) or pd.isnull(df['col_189']) or pd.isnull(df['col_190']) or pd.isnull(df['col_191']) or pd.isnull(df['col_192']) or pd.isnull(df['col_193']):
            if pd.isnull(float(df['col_194']) + float(df['col_195'])):
                return 'Inconsistent'
            elif pd.isnull(float(df['col_186']) + float(df['col_187']) + float(df['col_188']) + float(df['col_189']) + float(df['col_190']) + float(df['col_191']) + float(df['col_192']) + float(df['col_193'])):
                return 'Probable Reporting Error'
        elif float(df['col_194']) + float(df['col_195']) < float(df['col_186']) + float(df['col_187']) + float(df['col_188']) + float(df['col_189']) + float(df['col_190']) + float(df['col_191']) + float(df['col_192']) + float(df['col_193']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 14.3.3(200) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)
    def res47(df):
        if pd.isnull(df['col_200']) and pd.isnull(df['col_196']) and pd.isnull(df['col_197']) and pd.isnull(df['col_198']) and pd.isnull(df['col_199']):
            return 'Blank'
        elif pd.isnull(df['col_200']) or pd.isnull(df['col_196']) or pd.isnull(df['col_197']) or pd.isnull(df['col_198']) or pd.isnull(df['col_82']):
            if pd.isnull(df['col_200']):
                return 'Probable Reporting Error'
            elif pd.isnull((float(df['col_196']) + float(df['col_197']) + float(df['col_198']) + float(df['col_199']))):
                return 'Inconsistent'
        elif float(df['col_200']) > (float(df['col_196']) + float(df['col_197']) + float(df['col_198']) + float(df['col_199'])):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 14.5.2(210) <= 14.5.1(209)
    def res48(df):
        if pd.isnull(df['col_210']) and pd.isnull(df['col_209']):
            return 'Blank'
        elif pd.isnull(df['col_210']) or pd.isnull(df['col_209']):
            if pd.isnull(df['col_210']):
                return 'Probable Reporting Error'
            elif pd.isnull(df['col_209']):
                return 'Inconsistent'
        elif float(df['col_210']) > float(df['col_209']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 15.3.3.b(230) <= 15.3.3.a(229)
    def res49(df):
        if pd.isnull(df['col_230']) and pd.isnull(df['col_229']):
            return 'Blank'
        elif pd.isnull(df['col_230']) or pd.isnull(df['col_229']):
            if pd.isnull(df['col_230']):
                return 'Probable Reporting Error'
            elif pd.isnull(df['col_229']):
                return 'Inconsistent'
        elif float(df['col_230']) > float(df['col_229']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 15.3.3.c(231) <= 15.3.3.b(230)
    def res50(df):
        if pd.isnull(df['col_231']) and pd.isnull(df['col_230']):
            return 'Blank'
        elif pd.isnull(df['col_231']) or pd.isnull(df['col_230']):
            if pd.isnull(df['col_231']):
                return 'Probable Reporting Error'
            elif pd.isnull(df['col_230']):
                return 'Inconsistent'
        elif float(df['col_231']) > float(df['col_230']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 15.4.2(237) <= 15.4.1(236)
    def res51(df):
        if pd.isnull(df['col_237']) and pd.isnull(df['col_236']):
            return 'Blank'
        elif pd.isnull(df['col_237']) or pd.isnull(df['col_236']):
            if pd.isnull(df['col_237']):
                return 'Probable Reporting Error'
            elif pd.isnull(df['col_236']):
                return 'Inconsistent'
        elif float(df['col_237']) > float(df['col_236']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 9.6.1(142) <= 9.1.1(103) + 9.1.2(104) + 9.1.3(105) + 9.1.4(106) + 9.1.5(107) + 9.1.6(108) +9.1.7(109) + 9.1.8(110) + 9.1.13(115) + 9.1.14(116) + 9.1.15(117) + 9.1.16(118) + 9.1.17(119) + 9.1.18(120) + 9.1.19(121) + 9.1.20(122) + 9.1.21(123) + 9.2.1(124) + 9.2.2(125) + 9.2.3(126) + 9.3.1(129) + 9.3.2(130) + 9.3.3(131) + 9.4.1(132) + 9.4.2(133) + 9.4.3(134) + 9.4.5(136) + 9.4.6(137) + 9.5.1(138) + 9.5.2(139) + 9.5.3(140) + 9.5.4(141)
    def res52(df):
        if pd.isnull(df['col_142']) and pd.isnull(df['col_103']) and pd.isnull(df['col_104']) and pd.isnull(df['col_105']) and pd.isnull(df['col_106']) and pd.isnull(df['col_107']) and pd.isnull(df['col_108']) and pd.isnull(df['col_109']) and pd.isnull(df['col_110']) and pd.isnull(df['col_115']) and pd.isnull(df['col_116']) and pd.isnull(df['col_117']) and pd.isnull(df['col_118']) and pd.isnull(df['col_119']) and pd.isnull(df['col_120']) and pd.isnull(df['col_121']) and pd.isnull(df['col_122']) and pd.isnull(df['col_123']) and pd.isnull(df['col_124']) and pd.isnull(df['col_125']) and pd.isnull(df['col_126']) and pd.isnull(df['col_129']) and pd.isnull(df['col_130']) and pd.isnull(df['col_131']) and pd.isnull(df['col_132']) and pd.isnull(df['col_133']) and pd.isnull(df['col_134']) and pd.isnull(df['col_136']) and pd.isnull(df['col_137']) and pd.isnull(df['col_138']) and pd.isnull(df['col_139']) and pd.isnull(df['col_140']) and pd.isnull(df['col_141']) :
            return 'Blank'
        elif pd.isnull(df['col_142']) or pd.isnull(df['col_103']) or pd.isnull(df['col_104']) or pd.isnull(df['col_105']) or pd.isnull(df['col_106']) or pd.isnull(df['col_107']) or pd.isnull(df['col_108']) or pd.isnull(df['col_109']) or pd.isnull(df['col_110']) or pd.isnull(df['col_115']) or pd.isnull(df['col_116']) or pd.isnull(df['col_117']) or pd.isnull(df['col_118']) or pd.isnull(df['col_119']) or pd.isnull(df['col_120']) or pd.isnull(df['col_121']) or pd.isnull(df['col_122']) or pd.isnull(df['col_123']) or pd.isnull(df['col_124']) or pd.isnull(df['col_125']) or pd.isnull(df['col_126']) or pd.isnull(df['col_129']) or pd.isnull(df['col_130']) or pd.isnull(df['col_131']) or pd.isnull(df['col_132']) or pd.isnull(df['col_133']) or pd.isnull(df['col_134']) or pd.isnull(df['col_136']) or pd.isnull(df['col_137']) or pd.isnull(df['col_138']) or pd.isnull(df['col_139']) or pd.isnull(df['col_140']) or pd.isnull(df['col_141']) :
            if pd.isnull(df['col_142']):
                return 'Probable Reporting Error'
            elif pd.isnull(float(df['col_103']) + float(df['col_104']) + float(df['col_105']) + float(df['col_106']) + float(df['col_107']) + float(df['col_108']) + float(df['col_109']) + float(df['col_110']) + float(df['col_115']) + float(df['col_116']) + float(df['col_117']) + float(df['col_118']) + float(df['col_119']) + float(df['col_120']) + float(df['col_121']) + float(df['col_122']) + float(df['col_123']) + float(df['col_124']) + float(df['col_125']) + float(df['col_126']) + float(df['col_129']) + float(df['col_130']) + float(df['col_131']) + float(df['col_132']) + float(df['col_133']) + float(df['col_134']) + float(df['col_136']) + float(df['col_137']) + float(df['col_138']) + float(df['col_139']) + float(df['col_140']) + float(df['col_141'])):
                return 'Inconsistent'
        elif float(df['col_142']) > float(df['col_103']) + float(df['col_104']) + float(df['col_105']) + float(df['col_106']) + float(df['col_107']) + float(df['col_108']) + float(df['col_109']) + float(df['col_110']) + float(df['col_115']) + float(df['col_116']) + float(df['col_117']) + float(df['col_118']) + float(df['col_119']) + float(df['col_120']) + float(df['col_121']) + float(df['col_122']) + float(df['col_123']) + float(df['col_124']) + float(df['col_125']) + float(df['col_126']) + float(df['col_129']) + float(df['col_130']) + float(df['col_131']) + float(df['col_132']) + float(df['col_133']) + float(df['col_134']) + float(df['col_136']) + float(df['col_137']) + float(df['col_138']) + float(df['col_139']) + float(df['col_140']) + float(df['col_141']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df


    # 9.6.2(143) <= 9.1.1(103) + 9.1.2(104) + 9.1.3(105) + 9.1.4(106) + 9.1.5(107) + 9.1.6(108) +9.1.7(109) + 9.1.8(110) + 9.1.13(115) + 9.1.14(116) + 9.1.15(117) + 9.1.16(118) + 9.1.17(119) + 9.1.18(120) + 9.1.19(121) + 9.1.20(122) + 9.1.21(123) + 9.2.1(124) + 9.2.2(125) + 9.2.3(126) + 9.3.1(129) + 9.3.2(130) + 9.3.3(131) + 9.4.1(132) + 9.4.2(133) + 9.4.3(134) + 9.4.5(136) + 9.4.6(137) + 9.5.1(138) + 9.5.2(139) + 9.5.3(140) + 9.5.4(141)
    def res53(df):
        if pd.isnull(df['col_143']) and pd.isnull(df['col_103']) and pd.isnull(df['col_104']) and pd.isnull(df['col_105']) and pd.isnull(df['col_106']) and pd.isnull(df['col_107']) and pd.isnull(df['col_108']) and pd.isnull(df['col_109']) and pd.isnull(df['col_110']) and pd.isnull(df['col_115']) and pd.isnull(df['col_116']) and pd.isnull(df['col_117']) and pd.isnull(df['col_118']) and pd.isnull(df['col_119']) and pd.isnull(df['col_120']) and pd.isnull(df['col_121']) and pd.isnull(df['col_122']) and pd.isnull(df['col_123']) and pd.isnull(df['col_124']) and pd.isnull(df['col_125']) and pd.isnull(df['col_126']) and pd.isnull(df['col_129']) and pd.isnull(df['col_130']) and pd.isnull(df['col_131']) and pd.isnull(df['col_132']) and pd.isnull(df['col_133']) and pd.isnull(df['col_134']) and pd.isnull(df['col_136']) and pd.isnull(df['col_137']) and pd.isnull(df['col_138']) and pd.isnull(df['col_139']) and pd.isnull(df['col_140']) and pd.isnull(df['col_141']) :
            return 'Blank'
        elif pd.isnull(df['col_143']) or pd.isnull(df['col_103']) or pd.isnull(df['col_104']) or pd.isnull(df['col_105']) or pd.isnull(df['col_106']) or pd.isnull(df['col_107']) or pd.isnull(df['col_108']) or pd.isnull(df['col_109']) or pd.isnull(df['col_110']) or pd.isnull(df['col_115']) or pd.isnull(df['col_116']) or pd.isnull(df['col_117']) or pd.isnull(df['col_118']) or pd.isnull(df['col_119']) or pd.isnull(df['col_120']) or pd.isnull(df['col_121']) or pd.isnull(df['col_122']) or pd.isnull(df['col_123']) or pd.isnull(df['col_124']) or pd.isnull(df['col_125']) or pd.isnull(df['col_126']) or pd.isnull(df['col_129']) or pd.isnull(df['col_130']) or pd.isnull(df['col_131']) or pd.isnull(df['col_132']) or pd.isnull(df['col_133']) or pd.isnull(df['col_134']) or pd.isnull(df['col_136']) or pd.isnull(df['col_137']) or pd.isnull(df['col_138']) or pd.isnull(df['col_139']) or pd.isnull(df['col_140']) or pd.isnull(df['col_141']) :
            if pd.isnull(df['col_143']):
                return 'Probable Reporting Error'
            elif pd.isnull(float(df['col_103']) + float(df['col_104']) + float(df['col_105']) + float(df['col_106']) + float(df['col_107']) + float(df['col_108']) + float(df['col_109']) + float(df['col_110']) + float(df['col_115']) + float(df['col_116']) + float(df['col_117']) + float(df['col_118']) + float(df['col_119']) + float(df['col_120']) + float(df['col_121']) + float(df['col_122']) + float(df['col_123']) + float(df['col_124']) + float(df['col_125']) + float(df['col_126']) + float(df['col_129']) + float(df['col_130']) + float(df['col_131']) + float(df['col_132']) + float(df['col_133']) + float(df['col_134']) + float(df['col_136']) + float(df['col_137']) + float(df['col_138']) + float(df['col_139']) + float(df['col_140']) + float(df['col_141'])):
                return 'Inconsistent'
        elif float(df['col_143']) > float(df['col_103']) + float(df['col_104']) + float(df['col_105']) + float(df['col_106']) + float(df['col_107']) + float(df['col_108']) + float(df['col_109']) + float(df['col_110']) + float(df['col_115']) + float(df['col_116']) + float(df['col_117']) + float(df['col_118']) + float(df['col_119']) + float(df['col_120']) + float(df['col_121']) + float(df['col_122']) + float(df['col_123']) + float(df['col_124']) + float(df['col_125']) + float(df['col_126']) + float(df['col_129']) + float(df['col_130']) + float(df['col_131']) + float(df['col_132']) + float(df['col_133']) + float(df['col_134']) + float(df['col_136']) + float(df['col_137']) + float(df['col_138']) + float(df['col_139']) + float(df['col_140']) + float(df['col_141']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 9.6.3(144) <= 9.1.1(103) + 9.1.2(104) + 9.1.3(105) + 9.1.4(106) + 9.1.5(107) + 9.1.6(108) +9.1.7(109) + 9.1.8(110) + 9.1.13(115) + 9.1.14(116) + 9.1.15(117) + 9.1.16(118) + 9.1.17(119) + 9.1.18(120) + 9.1.19(121) + 9.1.20(122) + 9.1.21(123) + 9.2.1(124) + 9.2.2(125) + 9.2.3(126) + 9.3.1(129) + 9.3.2(130) + 9.3.3(131) + 9.4.1(132) + 9.4.2(133) + 9.4.3(134) + 9.4.5(136) + 9.4.6(137) + 9.5.1(138) + 9.5.2(139) + 9.5.3(140) + 9.5.4(141)
    def res54(df):
        if pd.isnull(df['col_144']) and pd.isnull(df['col_103']) and pd.isnull(df['col_104']) and pd.isnull(df['col_105']) and pd.isnull(df['col_106']) and pd.isnull(df['col_107']) and pd.isnull(df['col_108']) and pd.isnull(df['col_109']) and pd.isnull(df['col_110']) and pd.isnull(df['col_115']) and pd.isnull(df['col_116']) and pd.isnull(df['col_117']) and pd.isnull(df['col_118']) and pd.isnull(df['col_119']) and pd.isnull(df['col_120']) and pd.isnull(df['col_121']) and pd.isnull(df['col_122']) and pd.isnull(df['col_123']) and pd.isnull(df['col_124']) and pd.isnull(df['col_125']) and pd.isnull(df['col_126']) and pd.isnull(df['col_129']) and pd.isnull(df['col_130']) and pd.isnull(df['col_131']) and pd.isnull(df['col_132']) and pd.isnull(df['col_133']) and pd.isnull(df['col_134']) and pd.isnull(df['col_136']) and pd.isnull(df['col_137']) and pd.isnull(df['col_138']) and pd.isnull(df['col_139']) and pd.isnull(df['col_140']) and pd.isnull(df['col_141']) :
            return 'Blank'
        elif pd.isnull(df['col_144']) or pd.isnull(df['col_103']) or pd.isnull(df['col_104']) or pd.isnull(df['col_105']) or pd.isnull(df['col_106']) or pd.isnull(df['col_107']) or pd.isnull(df['col_108']) or pd.isnull(df['col_109']) or pd.isnull(df['col_110']) or pd.isnull(df['col_115']) or pd.isnull(df['col_116']) or pd.isnull(df['col_117']) or pd.isnull(df['col_118']) or pd.isnull(df['col_119']) or pd.isnull(df['col_120']) or pd.isnull(df['col_121']) or pd.isnull(df['col_122']) or pd.isnull(df['col_123']) or pd.isnull(df['col_124']) or pd.isnull(df['col_125']) or pd.isnull(df['col_126']) or pd.isnull(df['col_129']) or pd.isnull(df['col_130']) or pd.isnull(df['col_131']) or pd.isnull(df['col_132']) or pd.isnull(df['col_133']) or pd.isnull(df['col_134']) or pd.isnull(df['col_136']) or pd.isnull(df['col_137']) or pd.isnull(df['col_138']) or pd.isnull(df['col_139']) or pd.isnull(df['col_140']) or pd.isnull(df['col_141']) :
            if pd.isnull(df['col_144']):
                return 'Probable Reporting Error'
            elif pd.isnull(float(df['col_103']) + float(df['col_104']) + float(df['col_105']) + float(df['col_106']) + float(df['col_107']) + float(df['col_108']) + float(df['col_109']) + float(df['col_110']) + float(df['col_115']) + float(df['col_116']) + float(df['col_117']) + float(df['col_118']) + float(df['col_119']) + float(df['col_120']) + float(df['col_121']) + float(df['col_122']) + float(df['col_123']) + float(df['col_124']) + float(df['col_125']) + float(df['col_126']) + float(df['col_129']) + float(df['col_130']) + float(df['col_131']) + float(df['col_132']) + float(df['col_133']) + float(df['col_134']) + float(df['col_136']) + float(df['col_137']) + float(df['col_138']) + float(df['col_139']) + float(df['col_140']) + float(df['col_141'])):
                return 'Inconsistent'
        elif float(df['col_144']) > float(df['col_103']) + float(df['col_104']) + float(df['col_105']) + float(df['col_106']) + float(df['col_107']) + float(df['col_108']) + float(df['col_109']) + float(df['col_110']) + float(df['col_115']) + float(df['col_116']) + float(df['col_117']) + float(df['col_118']) + float(df['col_119']) + float(df['col_120']) + float(df['col_121']) + float(df['col_122']) + float(df['col_123']) + float(df['col_124']) + float(df['col_125']) + float(df['col_126']) + float(df['col_129']) + float(df['col_130']) + float(df['col_131']) + float(df['col_132']) + float(df['col_133']) + float(df['col_134']) + float(df['col_136']) + float(df['col_137']) + float(df['col_138']) + float(df['col_139']) + float(df['col_140']) + float(df['col_141']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 1.3.1.a(33) <= 1.3.1(32)
    def res55(df):
        if pd.isnull(df['col_33']) and pd.isnull(df['col_32']):
            return 'Blank'
        elif pd.isnull(df['col_33']) or pd.isnull(df['col_32']):
            if pd.isnull(df['col_33']):
                return 'Probable Reporting Error'
            elif pd.isnull(df['col_32']):
                return 'Inconsistent'
        elif float(df['col_33']) > float(df['col_32']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 9.7.2(146) <= 9.7.1(145)
    def res56(df):
        if pd.isnull(df['col_146']) and pd.isnull(df['col_145']):
            return 'Blank'
        elif pd.isnull(df['col_146']) or pd.isnull(df['col_145']):
            if pd.isnull(df['col_146']):
                return 'Probable Reporting Error'
            elif pd.isnull(df['col_145']):
                return 'Inconsistent'
        elif float(df['col_146']) > float(df['col_145']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 9.7.3(147) <= 9.7.2(146)
    def res57(df):
        if pd.isnull(df['col_147']) and pd.isnull(df['col_146']):
            return 'Blank'
        elif pd.isnull(df['col_147']) or pd.isnull(df['col_146']):
            if pd.isnull(df['col_147']):
                return 'Probable Reporting Error'
            elif pd.isnull(df['col_146']):
                return 'Inconsistent'
        elif float(df['col_147']) > float(df['col_146']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 11.1.1.b(169) <= 11.1.1.a(168)
    def res58(df):
        if pd.isnull(df['col_169']) and pd.isnull(df['col_168']):
            return 'Blank'
        elif pd.isnull(df['col_169']) or pd.isnull(df['col_168']):
            if pd.isnull(df['col_169']):
                return 'Probable Reporting Error'
            elif pd.isnull(df['col_168']):
                return 'Inconsistent'
        elif float(df['col_169']) > float(df['col_168']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 11.1.1.c(170) <= 11.1.1.a(168)
    def res59(df):
        if pd.isnull(df['col_170']) and pd.isnull(df['col_168']):
            return 'Blank'
        elif pd.isnull(df['col_170']) or pd.isnull(df['col_168']):
            if pd.isnull(df['col_170']):
                return 'Probable Reporting Error'
            elif pd.isnull(df['col_168']):
                return 'Inconsistent'
        elif float(df['col_170']) > float(df['col_168']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 11.1.2.b(171) <= 11.1.1.a(168)
    def res60(df):
        if pd.isnull(df['col_170']) and pd.isnull(df['col_168']):
            return 'Blank'
        elif pd.isnull(df['col_170']) or pd.isnull(df['col_168']):
            if pd.isnull(df['col_170']):
                return 'Probable Reporting Error'
            elif pd.isnull(df['col_168']):
                return 'Inconsistent'
        elif float(df['col_170']) > float(df['col_168']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 11.1.2.c(173) <= 11.1.2.a(171)
    def res61(df):
        if pd.isnull(df['col_173']) and pd.isnull(df['col_171']):
            return 'Blank'
        elif pd.isnull(df['col_173']) or pd.isnull(df['col_171']):
            if pd.isnull(df['col_173']):
                return 'Probable Reporting Error'
            elif pd.isnull(df['col_171']):
                return 'Inconsistent'
        elif float(df['col_173']) > float(df['col_171']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 14.4.1(201) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)
    def res62(df):
        if pd.isnull(df['col_201']) and pd.isnull(df['col_196']) and pd.isnull(df['col_197']) and pd.isnull(df['col_198']) and pd.isnull(df['col_199']):
            return 'Blank'
        elif pd.isnull(df['col_201']) or pd.isnull(df['col_196']) or pd.isnull(df['col_197']) or pd.isnull(df['col_198']) or pd.isnull(df['col_199']):
            if pd.isnull(df['col_201']):
                return 'Probable Reporting Error'
            elif pd.isnull((float(df['col_196']) + float(df['col_197']) + float(df['col_198']) + float(df['col_199']))):
                return 'Inconsistent'
        elif float(df['col_201']) > (float(df['col_196']) + float(df['col_197']) + float(df['col_198']) + float(df['col_199'])):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 14.4.2(202) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)
    def res63(df):
        if pd.isnull(df['col_202']) and pd.isnull(df['col_196']) and pd.isnull(df['col_197']) and pd.isnull(df['col_198']) and pd.isnull(df['col_199']):
            return 'Blank'
        elif pd.isnull(df['col_202']) or pd.isnull(df['col_196']) or pd.isnull(df['col_197']) or pd.isnull(df['col_198']) or pd.isnull(df['col_199']):
            if pd.isnull(df['col_202']):
                return 'Probable Reporting Error'
            elif pd.isnull((float(df['col_196']) + float(df['col_197']) + float(df['col_198']) + float(df['col_199']))):
                return 'Inconsistent'
        elif float(df['col_202']) > (float(df['col_196']) + float(df['col_197']) + float(df['col_198']) + float(df['col_199'])):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 14.4.3(203) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)
    def res64(df):
        if pd.isnull(df['col_203']) and pd.isnull(df['col_196']) and pd.isnull(df['col_197']) and pd.isnull(df['col_198']) and pd.isnull(df['col_199']):
            return 'Blank'
        elif pd.isnull(df['col_203']) or pd.isnull(df['col_196']) or pd.isnull(df['col_197']) or pd.isnull(df['col_198']) or pd.isnull(df['col_199']):
            if pd.isnull(df['col_203']):
                return 'Probable Reporting Error'
            elif pd.isnull((float(df['col_196']) + float(df['col_197']) + float(df['col_198']) + float(df['col_199']))):
                return 'Inconsistent'
        elif float(df['col_203']) > (float(df['col_196']) + float(df['col_197']) + float(df['col_198']) + float(df['col_199'])):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 14.4.4(204) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)
    def res65(df):
        if pd.isnull(df['col_204']) and pd.isnull(df['col_196']) and pd.isnull(df['col_197']) and pd.isnull(df['col_198']) and pd.isnull(df['col_199']):
            return 'Blank'
        elif pd.isnull(df['col_204']) or pd.isnull(df['col_196']) or pd.isnull(df['col_197']) or pd.isnull(df['col_198']) or pd.isnull(df['col_199']):
            if pd.isnull(df['col_204']):
                return 'Probable Reporting Error'
            elif pd.isnull((float(df['col_196']) + float(df['col_197']) + float(df['col_198']) + float(df['col_199']))):
                return 'Inconsistent'
        elif float(df['col_204']) > (float(df['col_196']) + float(df['col_197']) + float(df['col_198']) + float(df['col_199'])):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 14.4.5(205) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)
    def res66(df):
        if pd.isnull(df['col_205']) and pd.isnull(df['col_196']) and pd.isnull(df['col_197']) and pd.isnull(df['col_198']) and pd.isnull(df['col_199']):
            return 'Blank'
        elif pd.isnull(df['col_205']) or pd.isnull(df['col_196']) or pd.isnull(df['col_197']) or pd.isnull(df['col_198']) or pd.isnull(df['col_199']):
            if pd.isnull(df['col_205']):
                return 'Probable Reporting Error'
            elif pd.isnull((float(df['col_196']) + float(df['col_197']) + float(df['col_198']) + float(df['col_199']))):
                return 'Inconsistent'
        elif float(df['col_205']) > (float(df['col_196']) + float(df['col_197']) + float(df['col_198']) + float(df['col_199'])):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 14.4.6(206) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)
    def res67(df):
        if pd.isnull(df['col_206']) and pd.isnull(df['col_196']) and pd.isnull(df['col_197']) and pd.isnull(df['col_198']) and pd.isnull(df['col_199']):
            return 'Blank'
        elif pd.isnull(df['col_206']) or pd.isnull(df['col_196']) or pd.isnull(df['col_197']) or pd.isnull(df['col_198']) or pd.isnull(df['col_199']):
            if pd.isnull(df['col_206']):
                return 'Probable Reporting Error'
            elif pd.isnull((float(df['col_196']) + float(df['col_197']) + float(df['col_198']) + float(df['col_199']))):
                return 'Inconsistent'
        elif float(df['col_206']) > (float(df['col_196']) + float(df['col_197']) + float(df['col_198']) + float(df['col_199'])):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 14.4.7(207) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199))
    def res68(df):
        if pd.isnull(df['col_207']) and pd.isnull(df['col_196']) and pd.isnull(df['col_197']) and pd.isnull(df['col_198']) and pd.isnull(df['col_199']):
            return 'Blank'
        elif pd.isnull(df['col_207']) or pd.isnull(df['col_196']) or pd.isnull(df['col_197']) or pd.isnull(df['col_198']) or pd.isnull(df['col_199']):
            if pd.isnull(df['col_207']):
                return 'Probable Reporting Error'
            elif pd.isnull((float(df['col_196']) + float(df['col_197']) + float(df['col_198']) + float(df['col_199']))):
                return 'Inconsistent'
        elif float(df['col_207']) > (float(df['col_196']) + float(df['col_197']) + float(df['col_198']) + float(df['col_199'])):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 14.4.8(208) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)
    def res69(df):
        if pd.isnull(df['col_208']) and pd.isnull(df['col_196']) and pd.isnull(df['col_197']) and pd.isnull(df['col_198']) and pd.isnull(df['col_199']):
            return 'Blank'
        elif pd.isnull(df['col_208']) or pd.isnull(df['col_196']) or pd.isnull(df['col_197']) or pd.isnull(df['col_198']) or pd.isnull(df['col_199']):
            if pd.isnull(df['col_208']):
                return 'Probable Reporting Error'
            elif pd.isnull((float(df['col_196']) + float(df['col_197']) + float(df['col_198']) + float(df['col_199']))):
                return 'Inconsistent'
        elif float(df['col_208']) > (float(df['col_196']) + float(df['col_197']) + float(df['col_198']) + float(df['col_199'])):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 14.6.1(214) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)
    def res70(df):
        if pd.isnull(df['col_214']) and pd.isnull(df['col_196']) and pd.isnull(df['col_197']) and pd.isnull(df['col_198']) and pd.isnull(df['col_199']):
            return 'Blank'
        elif pd.isnull(df['col_214']) or pd.isnull(df['col_196']) or pd.isnull(df['col_197']) or pd.isnull(df['col_198']) or pd.isnull(df['col_199']):
            if pd.isnull(df['col_214']):
                return 'Probable Reporting Error'
            elif pd.isnull((float(df['col_196']) + float(df['col_197']) + float(df['col_198']) + float(df['col_199']))):
                return 'Inconsistent'
        elif float(df['col_214']) > (float(df['col_196']) + float(df['col_197']) + float(df['col_198']) + float(df['col_199'])):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 14.6.2(215) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)
    def res71(df):
        if pd.isnull(df['col_215']) and pd.isnull(df['col_196']) and pd.isnull(df['col_197']) and pd.isnull(df['col_198']) and pd.isnull(df['col_199']):
            return 'Blank'
        elif pd.isnull(df['col_215']) or pd.isnull(df['col_196']) or pd.isnull(df['col_197']) or pd.isnull(df['col_198']) or pd.isnull(df['col_199']):
            if pd.isnull(df['col_215']):
                return 'Probable Reporting Error'
            elif pd.isnull((float(df['col_196']) + float(df['col_197']) + float(df['col_198']) + float(df['col_199']))):
                return 'Inconsistent'
        elif float(df['col_215']) > (float(df['col_196']) + float(df['col_197']) + float(df['col_198']) + float(df['col_199'])):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 14.9.2(219) <= 14.9.1(218)
    def res72(df):
        if pd.isnull(df['col_219']) and pd.isnull(df['col_218']):
            return 'Blank'
        elif pd.isnull(df['col_219']) or pd.isnull(df['col_218']):
            if pd.isnull(df['col_219']):
                return 'Probable Reporting Error'
            elif pd.isnull(df['col_218']):
                return 'Inconsistent'
        elif float(df['col_219']) > float(df['col_218']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 15.2.2(224) <= 15.2.1(223)
    def res73(df):
        if pd.isnull(df['col_224']) and pd.isnull(df['col_223']):
            return 'Blank'
        elif pd.isnull(df['col_224']) or pd.isnull(df['col_223']):
            if pd.isnull(df['col_224']):
                return 'Probable Reporting Error'
            elif pd.isnull(df['col_223']):
                return 'Inconsistent'
        elif float(df['col_224']) > float(df['col_223']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 15.3.1.b(226) <= 15.3.1.a(225)
    def res74(df):
        if pd.isnull(df['col_226']) and pd.isnull(df['col_225']):
            return 'Blank'
        elif pd.isnull(df['col_226']) or pd.isnull(df['col_225']):
            if pd.isnull(df['col_226']):
                return 'Probable Reporting Error'
            elif pd.isnull(df['col_225']):
                return 'Inconsistent'
        elif float(df['col_226']) > float(df['col_225']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 15.3.2.b(228) <= 15.3.2.a(227)
    def res75(df):
        if pd.isnull(df['col_228']) and pd.isnull(df['col_227']):
            return 'Blank'
        elif pd.isnull(df['col_228']) or pd.isnull(df['col_227']):
            if pd.isnull(df['col_228']):
                return 'Probable Reporting Error'
            elif pd.isnull(df['col_227']):
                return 'Inconsistent'
        elif float(df['col_228']) > float(df['col_227']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 15.3.4.b(233) <= 15.3.4.a(232)
    def res76(df):
        if pd.isnull(df['col_233']) and pd.isnull(df['col_232']):
            return 'Blank'
        elif pd.isnull(df['col_233']) or pd.isnull(df['col_232']):
            if pd.isnull(df['col_233']):
                return 'Probable Reporting Error'
            elif pd.isnull(df['col_232']):
                return 'Inconsistent'
        elif float(df['col_232']) > float(df['col_233']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 15.3.4.d(235) <= 15.3.4.c(234)
    def res77(df):
        if pd.isnull(df['col_235']) and pd.isnull(df['col_234']):
            return 'Blank'
        elif pd.isnull(df['col_235']) or pd.isnull(df['col_234']):
            if pd.isnull(df['col_235']):
                return 'Probable Reporting Error'
            elif pd.isnull(df['col_234']):
                return 'Inconsistent'
        elif float(df['col_235']) > float(df['col_234']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    # 9.1.2(104) <= 4.1.1.a(56) + 4.1.1.b(57)
    def res78(df):
        if pd.isnull(df['col_104']) and pd.isnull(df['col_56']) and pd.isnull(df['col_57']):
            return 'Blank'
        elif pd.isnull(df['col_104']) or pd.isnull(df['col_56']) or pd.isnull(df['col_57']):
            if pd.isnull(df['col_104']):
                return 'Probable Reporting Error'
            elif pd.isnull((float(df['col_56']) + float(df['col_57']))):
                return 'Inconsistent'
        elif float(df['col_104']) > (float(df['col_56']) + float(df['col_57'])):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df



    # To count summary of the Modified Checks
    # =======================================

    df['9.1.1(103) <= 4.1.1.a(56) + 4.1.1.b(57)'] = df.apply(res1, axis=1)
    df['1.1.1(23) <= 1.1(22)'] = df.apply(res2, axis=1)
    df['1.2.4(27) <= 1.1(22)'] = df.apply(res3, axis=1)
    df['1.2.5(28) <= 1.1(22)'] = df.apply(res4, axis=1)
    df['1.2.7(30) <= 1.1(22)'] = df.apply(res5, axis=1)
    df['2.1.2(49) <= 2.1.1.a(47) + 2.1.1.b(48)'] = df.apply(res6, axis=1)
    df['2.1.3(50) <= 2.1.1.a(47) + 2.1.1.b(48)'] = df.apply(res7, axis=1)
    df['2.2.1(52) <= 2.2(51)'] = df.apply(res8, axis=1)
    df['2.2(51) >= 1.3.2(34)'] = df.apply(res9, axis=1)
    df['1.4.4(38) >= 1.4.3(37)'] = df.apply(res10, axis=1)
    df['1.5.1(39) <= 1.1(22)'] = df.apply(res11, axis=1)
    df['1.5.2(40) <= 1.5.1(39)'] = df.apply(res12, axis=1)
    df['1.5.3(41) <= 1.5.2(40)'] = df.apply(res13, axis=1)
    df['1.6.1.a(42) <= 1.1(22)'] = df.apply(res14, axis=1)
    df['1.6.1.b(43) <= 1.6.1.a(42)'] = df.apply(res15, axis=1)
    df['1.6.1.c(44) <= 1.6.1.b(43))'] = df.apply(res16, axis=1)
    df['1.6.1.e(46) <= 1.6.1.d(45)'] = df.apply(res17, axis=1)
    df['3.1.1(55) <= 2.2(51)'] = df.apply(res18, axis=1)
    df['3.1(54) <= 2.2(51)'] = df.apply(res19, axis=1)
    df['4.1.2(58) <= 4.1.1.a(56) + 4.1.1.b(57)'] = df.apply(res20, axis=1)
    df['4.1.1.a(56) + 4.1.1.b(57) + 4.1.3(59) >= 2.1.1.a(47) + 2.1.1.b(48) + 2.2(51)'] = df.apply(res21, axis=1)
    df['4.3.2.a(63) <= 4.3.1.a(61) + 4.3.1.b(62) + 4.2(60)'] = df.apply(res22, axis=1)
    df['4.3.2.b(64) <= 4.3.2.a(63)'] = df.apply(res23, axis=1)
    df['4.3.3(65) <= 4.3.1.a(61) + 4.3.1.b(62) + 4.2(60)'] = df.apply(res24, axis=1)
    df['4.4.1(66) <= 4.1.1.a(56) + 4.1.1.b(57)'] = df.apply(res25, axis=1)
    df['4.4.2(67) <= 4.4.1(66)'] = df.apply(res26, axis=1)
    df['4.4.3(68) <= 4.1.1.a(56) + 4.1.1.b(57)'] = df.apply(res27, axis=1)
    df['6.1(70) <= 2.1.1.a(47) + 2.1.1.b(48)'] = df.apply(res28, axis=1)
    df['6.3(72) <= 2.1.1.a(47) + 2.1.1.b(48) + 2.2(51)'] = df.apply(res29, axis=1)
    df['6.4(73) <= 2.1.1.a(47) + 2.1.1.b(48) + 2.2(51)'] = df.apply(res30, axis=1)
    df['7.2.1(76) <= 7.1.1(74)'] = df.apply(res31, axis=1)
    df['7.2.2(77) <= 7.1.2(75)'] = df.apply(res32, axis=1)
    df['8.2.3(81) <= 2.2(51)'] = df.apply(res33, axis=1)
    df['8.4(84) <= 2.1.1.a(47) + 2.1.1.b(48) + 2.2(51)'] = df.apply(res34, axis=1)
    df['8.7(87) <= 8.3(83) + 8.4(84) + 8.5(85)'] = df.apply(res35, axis=1)
    df['8.17.1(97) <= 8.1.1(78)'] = df.apply(res36, axis=1)
    df['8.17.2(98) <= 8.2.1(79) + 8.2.2(80) + 8.2.3(81) + 8.2.4(82)'] = df.apply(res37, axis=1)
    df['9.1.9(111) <= 4.1.1.a(56) + 4.1.1.b(57)'] = df.apply(res38, axis=1)
    df['9.1.13(115) <= 4.1.1.a(56) + 4.1.1.b(57)'] = df.apply(res39, axis=1)
    df['9.2.4.a(127) + 9.2.4.b(128) <= 9.2.1(124) + 9.2.2(125)'] = df.apply(res40, axis=1)
    df['11.2.2(175) <= 11.2.1(174)'] = df.apply(res41, axis=1)
    df['12.1.2.a(180) <= 12.1.1.a(178)'] = df.apply(res42, axis=1)
    df['12.1.2.b(181) <= 12.1.1.b(179)'] = df.apply(res43, axis=1)
    df['12.1.3.a(182) <= 12.1.1.a(178)'] = df.apply(res44, axis=1)
    df['12.1.3.b(183) <= 12.1.1.b(179)'] = df.apply(res45, axis=1)
    df['14.2.1(194) + 14.2.2(195) >= 14.1.1(186) + 14.1.2(187) + 14.1.3(188) + 14.1.4(189) + 14.1.5(190) + 14.1.6(191) + 14.1.7(192) + 14.1.8(193)'] = df.apply(res46, axis=1)
    df['14.3.3(200) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)'] = df.apply(res47, axis=1)
    df['14.5.2(210) <= 14.5.1(209)'] = df.apply(res48, axis=1)
    df['15.3.3.b(230) <= 15.3.3.a(229)'] = df.apply(res49, axis=1)
    df['15.3.3.c(231) <= 15.3.3.b(230))'] = df.apply(res50, axis=1)
    df['15.4.2(237) <= 15.4.1(236)'] = df.apply(res51, axis=1)
    df['9.6.1(142) <= 9.1.1(103) + 9.1.2(104) + 9.1.3(105) + 9.1.4(106) + 9.1.5(107) + 9.1.6(108) +9.1.7(109) + 9.1.8(110) + 9.1.13(115) + 9.1.14(116) + 9.1.15(117) + 9.1.16(118) + 9.1.17(119) + 9.1.18(120) + 9.1.19(121) + 9.1.20(122) + 9.1.21(123) + 9.2.1(124) + 9.2.2(125) + 9.2.3(126) + 9.3.1(129) + 9.3.2(130) + 9.3.3(131) + 9.4.1(132) + 9.4.2(133) + 9.4.3(134) + 9.4.5(136) + 9.4.6(137) + 9.5.1(138) + 9.5.2(139) + 9.5.3(140) + 9.5.4(141)'] = df.apply(res52, axis=1)
    df['9.6.2(143) <= 9.1.1(103) + 9.1.2(104) + 9.1.3(105) + 9.1.4(106) + 9.1.5(107) + 9.1.6(108) +9.1.7(109) + 9.1.8(110) + 9.1.13(115) + 9.1.14(116) + 9.1.15(117) + 9.1.16(118) + 9.1.17(119) + 9.1.18(120) + 9.1.19(121) + 9.1.20(122) + 9.1.21(123) + 9.2.1(124) + 9.2.2(125) + 9.2.3(126) + 9.3.1(129) + 9.3.2(130) + 9.3.3(131) + 9.4.1(132) + 9.4.2(133) + 9.4.3(134) + 9.4.5(136) + 9.4.6(137) + 9.5.1(138) + 9.5.2(139) + 9.5.3(140) + 9.5.4(141)'] = df.apply(res53, axis=1)
    df['9.6.3(144) <= 9.1.1(103) + 9.1.2(104) + 9.1.3(105) + 9.1.4(106) + 9.1.5(107) + 9.1.6(108) +9.1.7(109) + 9.1.8(110) + 9.1.13(115) + 9.1.14(116) + 9.1.15(117) + 9.1.16(118) + 9.1.17(119) + 9.1.18(120) + 9.1.19(121) + 9.1.20(122) + 9.1.21(123) + 9.2.1(124) + 9.2.2(125) + 9.2.3(126) + 9.3.1(129) + 9.3.2(130) + 9.3.3(131) + 9.4.1(132) + 9.4.2(133) + 9.4.3(134) + 9.4.5(136) + 9.4.6(137) + 9.5.1(138) + 9.5.2(139) + 9.5.3(140) + 9.5.4(141)'] = df.apply(res54, axis=1)
    df['1.3.1.a(33) <= 1.3.1(32)'] = df.apply(res55, axis=1)
    df['9.7.2(146) <= 9.7.1(145)'] = df.apply(res56, axis=1)
    df['9.7.3(147) <= 9.7.2(146)'] = df.apply(res57, axis=1)
    df['11.1.1.b(169) <= 11.1.1.a(168)'] = df.apply(res58, axis=1)
    df['11.1.1.c(170) <= 11.1.1.a(168)'] = df.apply(res59, axis=1)
    df['11.1.2.b(171) <= 11.1.1.a(168)'] = df.apply(res60, axis=1)
    df['11.1.2.c(173) <= 11.1.2.a(171)'] = df.apply(res61, axis=1)
    df['14.4.1(201) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)'] = df.apply(res62, axis=1)
    df['14.4.2(202) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199))'] = df.apply(res63, axis=1)
    df['14.4.3(203) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)'] = df.apply(res64, axis=1)
    df['14.4.4(204) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)'] = df.apply(res65, axis=1)
    df['14.4.5(205) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)'] = df.apply(res66, axis=1)
    df['14.4.6(206) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)'] = df.apply(res67, axis=1)
    df['14.4.7(207) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)'] = df.apply(res68, axis=1)
    df['14.4.8(208) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)'] = df.apply(res69, axis=1)
    df['14.6.1(214) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)'] = df.apply(res70, axis=1)
    df['14.6.2(215) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)'] = df.apply(res71, axis=1)
    df['14.9.2(219) <= 14.9.1(218)'] = df.apply(res72, axis=1)
    df['15.2.2(224) <= 15.2.1(223)'] = df.apply(res73, axis=1)
    df['15.3.1.b(226) <= 15.3.1.a(225)'] = df.apply(res74, axis=1)
    df['15.3.2.b(228) <= 15.3.2.a(227))'] = df.apply(res75, axis=1)
    df['15.3.4.b(233) <= 15.3.4.a(232)'] = df.apply(res76, axis=1)
    df['15.3.4.d(235) <= 15.3.4.c(234)'] = df.apply(res77, axis=1)
    df['9.1.2(104) <= 4.1.1.a(56) + 4.1.1.b(57)'] = df.apply(res78, axis=1)

    # Concatenating above renamed columns
    # ===================================
    df = pd.concat([df['9.1.1(103) <= 4.1.1.a(56) + 4.1.1.b(57)'],
                    df['1.1.1(23) <= 1.1(22)'],
                    df['1.2.4(27) <= 1.1(22)'],
                    df['1.2.5(28) <= 1.1(22)'],
                    df['1.2.7(30) <= 1.1(22)'],
                    df['2.1.2(49) <= 2.1.1.a(47) + 2.1.1.b(48)'],
                        df['2.1.3(50) <= 2.1.1.a(47) + 2.1.1.b(48)'],
                        df['2.2.1(52) <= 2.2(51)'],
                        df['2.2(51) >= 1.3.2(34)'],
                        df['1.4.4(38) >= 1.4.3(37)'],
                        df['1.5.1(39) <= 1.1(22)'],
                        df['1.5.2(40) <= 1.5.1(39)'],
                        df['1.5.3(41) <= 1.5.2(40)'],
                        df['1.6.1.a(42) <= 1.1(22)'],
                        df['1.6.1.b(43) <= 1.6.1.a(42)'],
                            df['1.6.1.c(44) <= 1.6.1.b(43))'],
                            df['1.6.1.e(46) <= 1.6.1.d(45)'],
                            df['3.1.1(55) <= 2.2(51)'],
                            df['3.1(54) <= 2.2(51)'],
                            df['4.1.2(58) <= 4.1.1.a(56) + 4.1.1.b(57)'],
                            df['4.1.1.a(56) + 4.1.1.b(57) + 4.1.3(59) >= 2.1.1.a(47) + 2.1.1.b(48) + 2.2(51)'],
                            df['4.3.2.a(63) <= 4.3.1.a(61) + 4.3.1.b(62) + 4.2(60)'],
                            df['4.3.2.b(64) <= 4.3.2.a(63)'],
                            df['4.3.3(65) <= 4.3.1.a(61) + 4.3.1.b(62) + 4.2(60)'],
                            df['4.4.1(66) <= 4.1.1.a(56) + 4.1.1.b(57)'],
                            df['4.4.2(67) <= 4.4.1(66)'],
                                df['4.4.3(68) <= 4.1.1.a(56) + 4.1.1.b(57)'],
                                df['6.1(70) <= 2.1.1.a(47) + 2.1.1.b(48)'],
                                df['6.3(72) <= 2.1.1.a(47) + 2.1.1.b(48) + 2.2(51)'],
                                df['6.4(73) <= 2.1.1.a(47) + 2.1.1.b(48) + 2.2(51)'],
                                df['7.2.1(76) <= 7.1.1(74)'],
                                df['7.2.2(77) <= 7.1.2(75)'],
                                df['8.2.3(81) <= 2.2(51)'],
                                df['8.4(84) <= 2.1.1.a(47) + 2.1.1.b(48) + 2.2(51)'],
                                df['8.7(87) <= 8.3(83) + 8.4(84) + 8.5(85)'],
                                df['8.17.1(97) <= 8.1.1(78)'],
                                df['8.17.2(98) <= 8.2.1(79) + 8.2.2(80) + 8.2.3(81) + 8.2.4(82)'],
                                    df['9.1.9(111) <= 4.1.1.a(56) + 4.1.1.b(57)'],
                                    df['9.1.13(115) <= 4.1.1.a(56) + 4.1.1.b(57)'],
                                    df['9.2.4.a(127) + 9.2.4.b(128) <= 9.2.1(124) + 9.2.2(125)'],
                                    df['11.2.2(175) <= 11.2.1(174)'],
                                    df['12.1.2.a(180) <= 12.1.1.a(178)'],
                                    df['12.1.2.b(181) <= 12.1.1.b(179)'],
                                    df['12.1.3.a(182) <= 12.1.1.a(178)'],
                                    df['12.1.3.b(183) <= 12.1.1.b(179)'],
                                    df['14.2.1(194) + 14.2.2(195) >= 14.1.1(186) + 14.1.2(187) + 14.1.3(188) + 14.1.4(189) + 14.1.5(190) + 14.1.6(191) + 14.1.7(192) + 14.1.8(193)'],
                                    df['14.3.3(200) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)'],
                                    df['14.5.2(210) <= 14.5.1(209)'],
                                    df['15.3.3.b(230) <= 15.3.3.a(229)'],
                                    df['15.3.3.c(231) <= 15.3.3.b(230))'],
                                        df['15.4.2(237) <= 15.4.1(236)'],
                                        df['9.6.1(142) <= 9.1.1(103) + 9.1.2(104) + 9.1.3(105) + 9.1.4(106) + 9.1.5(107) + 9.1.6(108) +9.1.7(109) + 9.1.8(110) + 9.1.13(115) + 9.1.14(116) + 9.1.15(117) + 9.1.16(118) + 9.1.17(119) + 9.1.18(120) + 9.1.19(121) + 9.1.20(122) + 9.1.21(123) + 9.2.1(124) + 9.2.2(125) + 9.2.3(126) + 9.3.1(129) + 9.3.2(130) + 9.3.3(131) + 9.4.1(132) + 9.4.2(133) + 9.4.3(134) + 9.4.5(136) + 9.4.6(137) + 9.5.1(138) + 9.5.2(139) + 9.5.3(140) + 9.5.4(141)'],
                                        df['9.6.2(143) <= 9.1.1(103) + 9.1.2(104) + 9.1.3(105) + 9.1.4(106) + 9.1.5(107) + 9.1.6(108) +9.1.7(109) + 9.1.8(110) + 9.1.13(115) + 9.1.14(116) + 9.1.15(117) + 9.1.16(118) + 9.1.17(119) + 9.1.18(120) + 9.1.19(121) + 9.1.20(122) + 9.1.21(123) + 9.2.1(124) + 9.2.2(125) + 9.2.3(126) + 9.3.1(129) + 9.3.2(130) + 9.3.3(131) + 9.4.1(132) + 9.4.2(133) + 9.4.3(134) + 9.4.5(136) + 9.4.6(137) + 9.5.1(138) + 9.5.2(139) + 9.5.3(140) + 9.5.4(141)'],
                                        df['9.6.3(144) <= 9.1.1(103) + 9.1.2(104) + 9.1.3(105) + 9.1.4(106) + 9.1.5(107) + 9.1.6(108) +9.1.7(109) + 9.1.8(110) + 9.1.13(115) + 9.1.14(116) + 9.1.15(117) + 9.1.16(118) + 9.1.17(119) + 9.1.18(120) + 9.1.19(121) + 9.1.20(122) + 9.1.21(123) + 9.2.1(124) + 9.2.2(125) + 9.2.3(126) + 9.3.1(129) + 9.3.2(130) + 9.3.3(131) + 9.4.1(132) + 9.4.2(133) + 9.4.3(134) + 9.4.5(136) + 9.4.6(137) + 9.5.1(138) + 9.5.2(139) + 9.5.3(140) + 9.5.4(141)'],
                                        df['1.3.1.a(33) <= 1.3.1(32)'],
                                        df['9.7.2(146) <= 9.7.1(145)'],
                                        df['9.7.3(147) <= 9.7.2(146)'],
                                        df['11.1.1.b(169) <= 11.1.1.a(168)'],
                                        df['11.1.1.c(170) <= 11.1.1.a(168)'],
                                        df['11.1.2.b(171) <= 11.1.1.a(168)'],
                                        df['11.1.2.c(173) <= 11.1.2.a(171)'],
                                        df['14.4.1(201) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)'],
                                            df['14.4.2(202) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199))'],
                                            df['14.4.3(203) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)'],
                                            df['14.4.4(204) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)'],
                                            df['14.4.5(205) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)'],
                                            df['14.4.6(206) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)'],
                                            df['14.4.7(207) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)'],
                                            df['14.4.8(208) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)'],
                                            df['14.6.1(214) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)'],
                                            df['14.6.2(215) <= 14.3.1.a(196) + 14.3.1.b(197) + 14.3.2.a(198) + 14.3.2.b(199)'],
                                            df['14.9.2(219) <= 14.9.1(218)'],
                                                df['15.2.2(224) <= 15.2.1(223)'],
                                                df['15.3.1.b(226) <= 15.3.1.a(225)'],
                                                df['15.3.2.b(228) <= 15.3.2.a(227))'],
                                                df['15.3.4.b(233) <= 15.3.4.a(232)'],
                                                df['15.3.4.d(235) <= 15.3.4.c(234)'],
                                                df['9.1.2(104) <= 4.1.1.a(56) + 4.1.1.b(57)']], axis=1)

    # Mergining current result of modified checks with original dataframe and displaying it on screen
    frames = [df_, df]
    
    df = pd.concat(frames, axis=1, sort=False)
    print(df)
    # Create the messagebox object
    self.msg = QMessageBox()
    # Set the information icon
    self.msg.setWindowIcon(QtGui.QIcon('checked.png'))
    self.msg.setStyleSheet("QLabel {border: 2px solid green; margin-right: 15px ; font-size: 18px; font-family: Arial;} QPushButton {background-color:lightgreen; font-family: Arial; font-size:20px;} ")
    # Set the main message
    self.msg.setText("Primary Health Centre validation successfully complete.")
    # Set the title of the window
    self.msg.setWindowTitle("Validation Successful Message")
    # Display the message box
    self.msg.show()

    return df


# To reference df
def load_PHC(self):
    return df