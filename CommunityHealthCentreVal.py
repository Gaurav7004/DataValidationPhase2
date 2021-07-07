import pandas as pd
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox

# Community Health Centers Validation Rules Function
# ===============================================
def CHC_Validate(self, df_):
    global df

    # df = self.loadFile(df_)
    df = df_
    filterString = self.lineEdit_2.text()
    
    df = df_.loc[df_['col_12'] == filterString]
    #df = df.dropna(subset=['col_18', 'col_19'], inplace=True)
    print('Entered CHC_Validate')

    # Modified Checks of SDH

    #1.1.1(23) <= 1.1(22)
    def res1(df):
        if pd.isnull(df['col_23']) and pd.isnull(df['col_22']):
            return 'Blank'
        elif pd.isnull(df['col_23']) or pd.isnull(df['col_22']):
            if pd.isnull(df['col_23']):
                return 'Probable Reporting Error(1.1.1 is blank)'
            elif pd.isnull(float(df['col_22'])):
                return 'Inconsistent'
        elif float(df['col_23']) > float(df['col_22']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #15.3.1.b(237) <= 15.3.1.a(236)
    def res2(df):
        if pd.isnull(df['col_237']) and pd.isnull(df['col_236']):
            return 'Blank'
        elif pd.isnull(df['col_237']) or pd.isnull(df['col_236']):
            if pd.isnull(df['col_237']):
                return 'Probable Reporting Error(15.3.1.b is blank)'
            elif pd.isnull(float(df['col_236'])):
                return 'Inconsistent'
        elif float(df['col_237']) > float(df['col_236']):
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
    
    
    #1.2.5(28) <= 1.1(22)
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
    
    #1.2.7(30) <= 1.1(22)
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
    
    #1.3.1.a(33) <= 1.3.1(32)
    def res6(df):
        if pd.isnull(df['col_33']) and pd.isnull(df['col_32']):
            return 'Blank'
        elif pd.isnull(df['col_33']) or pd.isnull(df['col_32']):
            if pd.isnull(df['col_33']):
                return 'Probable Reporting Error(1.3.1.a is blank)'
            elif pd.isnull(float(df['col_32'])):
                return 'Inconsistent'
        elif float(df['col_33']) > float(df['col_32']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #1.3.2(34) <= 2.1(47)
    def res7(df):
        if pd.isnull(df['col_34']) and pd.isnull(df['col_47']):
            return 'Blank'
        elif pd.isnull(df['col_34']) or pd.isnull(df['col_47']):
            if pd.isnull(df['col_34']):
                return 'Probable Reporting Error(1.3.2 is blank)'
            elif pd.isnull(float(df['col_47'])):
                return 'Inconsistent'
        elif float(df['col_34']) > float(df['col_47']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #1.4.4(38) >= 1.4.3(37)
    def res8(df):
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

            if lhs_value >= rhs_value:
                if lhs_value > (0.5*rhs_value):
                    return 'Probable Reporting Error'
                else:
                    return 'consistent'
            else:
                if lhs_value < (0.5*rhs_value):
                    return 'Probable Reporting Error'
                else:
                    return 'Inconsistent'
        return df
    
    #1.5.2(40) <= 1.5.1(39)
    def res9(df):
        if pd.isnull(df['col_40']) and pd.isnull(df['col_39']):
            return 'Blank'
        elif pd.isnull(df['col_40']) or pd.isnull(df['col_39']):
            if pd.isnull(df['col_40']):
                return 'Probable Reporting Error(1.5.2 is blank)'
            elif pd.isnull(float(df['col_39'])):
                return 'Inconsistent'
        elif float(df['col_40']) > float(df['col_39']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    
    #1.5.1(39) <= 1.1(22)
    def res10(df):
        if pd.isnull(df['col_39']) and pd.isnull(df['col_22']):
            return 'Blank'
        elif pd.isnull(df['col_39']) or pd.isnull(df['col_22']):
            if pd.isnull(df['col_39']):
                return 'Probable Reporting Error(1.5.1 is blank)'
            elif pd.isnull(float(df['col_22'])):
                return 'Inconsistent'
        elif float(df['col_39']) > float(df['col_22']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #1.5.3(41) <= 1.5.2(40)
    def res11(df):
        if pd.isnull(df['col_41']) and pd.isnull(df['col_40']):
            return 'Blank'
        elif pd.isnull(df['col_41']) or pd.isnull(df['col_40']):
            if pd.isnull(df['col_41']):
                return 'Probable Reporting Error(1.5.3 is blank)'
            elif pd.isnull(float(df['col_40'])):
                return 'Inconsistent'
        elif float(df['col_41']) > float(df['col_40']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #1.6.1.b(43) <= 1.6.1.a(42)
    def res12(df):
        if pd.isnull(df['col_43']) and pd.isnull(df['col_42']):
            return 'Blank'
        elif pd.isnull(df['col_43']) or pd.isnull(df['col_42']):
            if pd.isnull(df['col_43']):
                return 'Probable Reporting Error(1.6.1.b is blank)'
            elif pd.isnull(float(df['col_42'])):
                return 'Inconsistent'
        elif float(df['col_43']) > float(df['col_42']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #1.6.1.a(42) <= 1.1(22)
    def res13(df):
        if pd.isnull(df['col_42']) and pd.isnull(df['col_22']):
            return 'Blank'
        elif pd.isnull(df['col_42']) or pd.isnull(df['col_22']):
            if pd.isnull(df['col_42']):
                return 'Probable Reporting Error(1.6.1 is blank)'
            elif pd.isnull(float(df['col_22'])):
                return 'Inconsistent'
        elif float(df['col_42']) > float(df['col_22']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #1.6.1.c(44) <= 1.6.1.b(43)
    def res14(df):
        if pd.isnull(df['col_44']) and pd.isnull(df['col_43']):
            return 'Blank'
        elif pd.isnull(df['col_44']) or pd.isnull(df['col_43']):
            if pd.isnull(df['col_44']):
                return 'Probable Reporting Error(1.6.1.c is blank)'
            elif pd.isnull(float(df['col_43'])):
                return 'Inconsistent'
        elif float(df['col_44']) > float(df['col_43']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #1.6.1.e(46) <= 1.6.1.d(45)
    def res15(df):
        if pd.isnull(df['col_46']) and pd.isnull(df['col_45']):
            return 'Blank'
        elif pd.isnull(df['col_46']) or pd.isnull(df['col_45']):
            if pd.isnull(df['col_46']):
                return 'Probable Reporting Error(1.6.1.e is blank)'
            elif pd.isnull(float(df['col_45'])):
                return 'Inconsistent'
        elif float(df['col_46']) > float(df['col_45']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #2.1.1(48) <= 2.1(47)
    def res16(df):
        if pd.isnull(df['col_48']) and pd.isnull(df['col_47']):
            return 'Blank'
        elif pd.isnull(df['col_48']) or pd.isnull(df['col_47']):
            if pd.isnull(df['col_48']):
                return 'Probable Reporting Error(2.1.1 is blank)'
            elif pd.isnull(float(df['col_47'])):
                return 'Inconsistent'
        elif float(df['col_48']) > float(df['col_47']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #3.1(50) <= 2.1(47)
    def res17(df):
        if pd.isnull(df['col_50']) and pd.isnull(df['col_47']):
            return 'Blank'
        elif pd.isnull(df['col_50']) or pd.isnull(df['col_47']):
            if pd.isnull(df['col_50']):
                return 'Probable Reporting Error(3.1 is blank)'
            elif pd.isnull(float(df['col_47'])):
                return 'Inconsistent'
        elif float(df['col_50']) > float(df['col_47']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #3.1.1(51) <= 3.1(50)
    def res18(df):
        if pd.isnull(df['col_51']) and pd.isnull(df['col_50']):
            return 'Blank'
        elif pd.isnull(df['col_51']) or pd.isnull(df['col_50']):
            if pd.isnull(df['col_51']):
                return 'Probable Reporting Error(3.1.1 is blank)'
            elif pd.isnull(float(df['col_50'])):
                return 'Inconsistent'
        elif float(df['col_51']) > float(df['col_50']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #4.1.1.a(52) + 4.1.1.b(53) + 4.1.3(55) >= 2.1(47)
    def res19(df):
        if pd.isnull(df['col_52']) and pd.isnull(df['col_53']) and pd.isnull(df['col_55']) and pd.isnull(df['col_47']):
            return 'Blank'
        elif pd.isnull(df['col_52']) or pd.isnull(df['col_53']) or pd.isnull(df['col_55']) or pd.isnull(df['col_47']):
            if pd.isnull((float(df['col_52'])) + (float(df['col_53'])) + (float(df['col_55']))) and not pd.isnull(float(df['col_47'])):
                return 'Inconsistent'
            elif not pd.isnull((float(df['col_52'])) + (float(df['col_53'])) + (float(df['col_55']))) and pd.isnull(float(df['col_47'])):
                return 'Probable Reporting Error'
        elif float(df['col_47']) > float(df['col_52']) + float(df['col_53']) + float(df['col_55']) :
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #4.1.2(54) <= 4.1.1.a(52) + 4.1.1.b(53)
    def res20(df):
        if pd.isnull(df['col_54']) and pd.isnull(df['col_52']) and pd.isnull(df['col_53']):
            return 'Blank'
        elif pd.isnull(df['col_54']) or pd.isnull(df['col_52']) or pd.isnull(df['col_53']):
            if pd.isnull(df['col_54']):
                return 'Probable Reporting Error(4.1.2 is blank)'
            elif pd.isnull((float(df['col_52']) + float(df['col_53']))):
                return 'Inconsistent'
        elif float(df['col_54']) > float(df['col_52']) + float(df['col_53']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #4.3.2.a(59) <= 4.3.1.a(57) + 4.3.1.b(58) + 4.2(56)
    def res21(df):
        if pd.isnull(df['col_59']) and pd.isnull(df['col_57']) and pd.isnull(df['col_58']) and pd.isnull(df['col_56']):
            return 'Blank'
        elif pd.isnull(df['col_59']) or pd.isnull(df['col_57']) or pd.isnull(df['col_58']) or pd.isnull(df['col_56']):
            if pd.isnull(df['col_59']):
                return 'Probable Reporting Error(4.3.2.a is blank)'
            elif pd.isnull((float(df['col_57']) + float(df['col_58']) + float(df['col_56']))):
                return 'Inconsistent'
        elif float(df['col_59']) > float(df['col_57']) + float(df['col_58']) + float(df['col_56']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #4.3.2.b(60) <= 4.3.2.a(59)
    def res22(df):
        if pd.isnull(df['col_60']) and pd.isnull(df['col_59']):
            return 'Blank'
        elif pd.isnull(df['col_60']) or pd.isnull(df['col_59']):
            if pd.isnull(df['col_60']):
                return 'Probable Reporting Error(4.3.2.b is blank)'
            elif pd.isnull((float(df['col_59']))):
                return 'Inconsistent'
        elif float(df['col_60']) > float(df['col_59']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #4.3.3(61) <= 4.3.1.a(57) + 4.3.1.b(58) + 4.2(56)
    def res23(df):
        if pd.isnull(df['col_61']) and pd.isnull(df['col_57']) and pd.isnull(df['col_58']) and pd.isnull(df['col_56']):
            return 'Blank'
        elif pd.isnull(df['col_61']) or pd.isnull(df['col_57']) or pd.isnull(df['col_58']) or pd.isnull(df['col_56']):
            if pd.isnull(df['col_61']):
                return 'Probable Reporting Error(4.3.3 is blank)'
            elif pd.isnull((float(df['col_57'])) + (float(df['col_58'])) + (float(df['col_56']))):
                return 'Inconsistent'
        elif float(df['col_61']) > float(df['col_57']) + float(df['col_58']) + float(df['col_56']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #4.4.1(62) <= 4.1.1.a(52) + 4.1.1.b(53)
    def res24(df):
        if pd.isnull(df['col_62']) and pd.isnull(df['col_52']) and pd.isnull(df['col_53']):
            return 'Blank'
        elif pd.isnull(df['col_62']) or pd.isnull(df['col_52']) or pd.isnull(df['col_53']):
            if pd.isnull(df['col_62']):
                return 'Probable Reporting Error(4.4.1 is blank)'
            elif pd.isnull((float(df['col_52'])) + (float(df['col_53']))):
                return 'Inconsistent'
        elif float(df['col_62']) > float(df['col_52']) + float(df['col_53']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #4.4.2(63) <= 4.4.1(62)
    def res25(df):
        if pd.isnull(df['col_63']) and pd.isnull(df['col_62']):
            return 'Blank'
        elif pd.isnull(df['col_63']) or pd.isnull(df['col_62']):
            if pd.isnull(df['col_63']):
                return 'Probable Reporting Error(4.4.2 is blank)'
            elif pd.isnull((float(df['col_62']))):
                return 'Inconsistent'
        elif float(df['col_63']) > float(df['col_62']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #4.4.3(64) <= 4.1.1.a(52) + 4.1.1.b(53)
    def res26(df):
        if pd.isnull(df['col_64']) and pd.isnull(df['col_52']) and pd.isnull(df['col_53']):
            return 'Blank'
        elif pd.isnull(df['col_64']) or pd.isnull(df['col_52']) or pd.isnull(df['col_53']):
            if pd.isnull(df['col_64']):
                return 'Probable Reporting Error(4.4.3 is blank)'
            elif pd.isnull((float(df['col_52'])) + (float(df['col_53']))):
                return 'Inconsistent'
        elif float(df['col_64']) > float(df['col_52']) + float(df['col_53']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #5.2(66) <= 5.1(65)
    def res27(df):
        if pd.isnull(df['col_66']) and pd.isnull(df['col_65']):
            return 'Blank'
        elif pd.isnull(df['col_66']) or pd.isnull(df['col_65']):
            if pd.isnull(df['col_66']):
                return 'Probable Reporting Error(5.2 is blank)'
            elif pd.isnull((float(df['col_65']))):
                return 'Inconsistent'
        elif float(df['col_66']) > float(df['col_65']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #6.3(69) <= 2.1(47)
    def res28(df):
        if pd.isnull(df['col_69']) and pd.isnull(df['col_47']):
            return 'Blank'
        elif pd.isnull(df['col_69']) or pd.isnull(df['col_47']):
            if pd.isnull(df['col_69']) and not pd.isnull(float(df['col_47'])):
                return 'Probable Reporting Error'
            else:
                return 'Probable Reporting Error'
            
            # If value exists for all the elements
        else:

            lhs_value = float(df['col_69'])
            rhs_value = float(df['col_47'])

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
    
    #6.4(70) <= 2.1(47)
    def res29(df):
        if pd.isnull(df['col_70']) and pd.isnull(df['col_47']):
            return 'Blank'
        elif pd.isnull(df['col_70']) or pd.isnull(df['col_47']):
            if pd.isnull(df['col_70']) and not pd.isnull(float(df['col_47'])):
                return 'Probable Reporting Error'
            else:
                return 'Probable Reporting Error'
            
            # If value exists for all the elements
        else:

            lhs_value = float(df['col_70'])
            rhs_value = float(df['col_47'])

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
    
    #7.2.1(73) <= 7.1.1(71)
    def res30(df):
        if pd.isnull(df['col_73']) and pd.isnull(df['col_71']):
            return 'Blank'
        elif pd.isnull(df['col_73']) or pd.isnull(df['col_71']):
            if pd.isnull(df['col_73']):
                return 'Probable Reporting Error(7.2.1 is blank)'
            elif pd.isnull((float(df['col_71']))):
                return 'Inconsistent'
        elif float(df['col_73']) > float(df['col_71']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #7.2.2(74) <= 7.1.2(72)
    def res31(df):
        if pd.isnull(df['col_74']) and pd.isnull(df['col_72']):
            return 'Blank'
        elif pd.isnull(df['col_74']) or pd.isnull(df['col_72']):
            if pd.isnull(df['col_74']):
                return 'Probable Reporting Error(7.2.2 is blank)'
            elif pd.isnull((float(df['col_72']))):
                return 'Inconsistent'
        elif float(df['col_74']) > float(df['col_72']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #8.2.3(78) <= 2.1(47)
    def res32(df):
        if pd.isnull(df['col_78']) and pd.isnull(df['col_47']):
            return 'Blank'
        elif pd.isnull(df['col_78']) or pd.isnull(df['col_47']):
            if pd.isnull(df['col_78']):
                return 'Probable Reporting Error(8.2.3 is blank)'
            elif pd.isnull((float(df['col_47']))):
                return 'Inconsistent'
        elif float(df['col_78']) > float(df['col_47']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
        #8.4(81) <= 2.1(47)
    def res33(df):
        if pd.isnull(df['col_81']) and pd.isnull(df['col_47']):
            return 'Blank'
        elif pd.isnull(df['col_81']) or pd.isnull(df['col_47']):
            if pd.isnull(df['col_81']):
                return 'Probable Reporting Error(8.4 is blank)'
            elif pd.isnull((float(df['col_47']))):
                return 'Inconsistent'
        elif float(df['col_81']) > float(df['col_47']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #8.7(84) <= 8.3(80) + 8.4(81) + 8.5(82)
    def res34(df):
        if pd.isnull(df['col_84']) and pd.isnull(df['col_80']) and pd.isnull(df['col_81']) and pd.isnull(df['col_82']):
            return 'Blank'
        elif pd.isnull(df['col_84']) or pd.isnull(df['col_80']) or pd.isnull(df['col_81']) or pd.isnull(df['col_82']):
            if pd.isnull(df['col_84']):
                return 'Probable Reporting Error(8.7 is blank)'
            elif pd.isnull((float(df['col_80'])) + (float(df['col_81'])) + (float(df['col_82']))):
                return 'Inconsistent'
        elif float(df['col_84']) > float(df['col_80']) + float(df['col_81']) + float(df['col_82']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #8.17.1(94) <= 8.1.1(75)
    def res35(df):
        if pd.isnull(df['col_94']) and pd.isnull(df['col_75']):
            return 'Blank'
        elif pd.isnull(df['col_94']) or pd.isnull(df['col_75']):
            if pd.isnull(df['col_94']):
                return 'Probable Reporting Error(8.17.1 is blank)'
            elif pd.isnull((float(df['col_75']))):
                return 'Inconsistent'
        elif float(df['col_94']) > float(df['col_75']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #8.17.2(95) <= 8.2.1(76) + 8.2.2(77) + 8.2.3(78) + 8.2.4(79)
    def res36(df):
        if pd.isnull(df['col_95']) and pd.isnull(df['col_76']) and pd.isnull(df['col_77']) and pd.isnull(df['col_78']) and pd.isnull(df['col_79']):
            return 'Blank'
        elif pd.isnull(df['col_95']) or pd.isnull(df['col_76']) or pd.isnull(df['col_77']) or pd.isnull(df['col_78']) or pd.isnull(df['col_79']):
            if pd.isnull(df['col_95']):
                return 'Probable Reporting Error(8.17.2 is blank)'
            elif pd.isnull((float(df['col_76'])) + (float(df['col_77'])) + (float(df['col_78'])) + (float(df['col_79']))):
                return 'Inconsistent'
        elif float(df['col_95']) > float(df['col_76']) + float(df['col_77']) + float(df['col_78']) + float(df['col_79']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #9.1.1(100) <= 4.1.1.a(52) + 4.1.1.b(53)
    def res37(df):
        if pd.isnull(df['col_100']) and pd.isnull(df['col_52']) and pd.isnull(df['col_53']):
            return 'Blank'
        elif pd.isnull(df['col_100']) or pd.isnull(df['col_52']) or pd.isnull(df['col_53']):
            if pd.isnull(df['col_100']):
                return 'Probable Reporting Error(9.1.1 is blank)'
            elif pd.isnull((float(df['col_52'])) + (float(df['col_53']))):
                return 'Inconsistent'
        elif float(df['col_100']) > float(df['col_52']) + float(df['col_53']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #9.1.2(101) <= 4.1.1.a(52) + 4.1.1.b(53)
    def res38(df):
        if pd.isnull(df['col_101']) and pd.isnull(df['col_52']) and pd.isnull(df['col_53']):
            return 'Blank'
        elif pd.isnull(df['col_101']) or pd.isnull(df['col_52']) or pd.isnull(df['col_53']):
            if pd.isnull(df['col_101']):
                return 'Probable Reporting Error(9.1.2 is blank)'
            elif pd.isnull((float(df['col_52'])) + (float(df['col_53']))):
                return 'Inconsistent'
        elif float(df['col_101']) > float(df['col_52']) + float(df['col_53']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #9.1.9(108) <= 4.1.1.a(52) + 4.1.1.b(53)
    def res39(df):
        if pd.isnull(df['col_108']) and pd.isnull(df['col_52']) and pd.isnull(df['col_53']):
            return 'Blank'
        elif pd.isnull(df['col_108']) or pd.isnull(df['col_52']) or pd.isnull(df['col_53']):
            if pd.isnull(df['col_108']):
                return 'Probable Reporting Error(9.1.9 is blank)'
            elif pd.isnull((float(df['col_52'])) + (float(df['col_53']))):
                return 'Inconsistent'
        elif float(df['col_108']) > float(df['col_52']) + float(df['col_53']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #9.1.13(112) <= 4.1.1.a(52) + 4.1.1.b(53)
    def res40(df):
        if pd.isnull(df['col_112']) and pd.isnull(df['col_52']) and pd.isnull(df['col_53']):
            return 'Blank'
        elif pd.isnull(df['col_112']) or pd.isnull(df['col_52']) or pd.isnull(df['col_53']):
            if pd.isnull(df['col_112']):
                return 'Probable Reporting Error(9.1.13 is blank)'
            elif pd.isnull((float(df['col_52'])) + (float(df['col_53']))):
                return 'Inconsistent'
        elif float(df['col_112']) > float(df['col_52']) + float(df['col_53']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #9.2.4.a(124) + 9.2.4.b(125) <= 9.2.1(121) + 9.2.2(122)
    def res41(df):
        if pd.isnull(df['col_124']) and pd.isnull(df['col_125']) and pd.isnull(df['col_121']) and pd.isnull(df['col_122']):
            return 'Blank'
        elif pd.isnull(df['col_124']) or pd.isnull(df['col_125']) or pd.isnull(df['col_121']) or pd.isnull(df['col_122']):
            if pd.isnull((float(df['col_124'])) + (float(df['col_125']))) and not pd.isnull(float(df['col_121']) + float(df['col_122'])):
                return 'Probable Reporting Error'
            elif not pd.isnull((float(df['col_124'])) + (float(df['col_125']))) and pd.isnull(float(df['col_121']) + float(df['col_122'])):
                return 'Inconsistent'
        elif (float(df['col_124']) + float(df['col_125'])) > (float(df['col_121']) + float(df['col_122'])):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #11.2.2(172) <= 11.2.1(171)
    def res42(df):
        if pd.isnull(df['col_172']) and pd.isnull(df['col_171']):
            return 'Blank'
        elif pd.isnull(df['col_172']) or pd.isnull(df['col_171']):
            if pd.isnull(df['col_172']):
                return 'Probable Reporting Error(11.2.2 is blank)'
            elif pd.isnull((float(df['col_171']))):
                return 'Inconsistent'
        elif float(df['col_172']) > float(df['col_171']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
        #12.1.2.a(177) <= 12.1.1.a(175)
    def res43(df):
        if pd.isnull(df['col_177']) and pd.isnull(df['col_175']):
            return 'Blank'
        elif pd.isnull(df['col_177']) or pd.isnull(df['col_175']):
            if pd.isnull(df['col_177']):
                return 'Probable Reporting Error(12.1.2.a is blank)'
            elif pd.isnull((float(df['col_175']))):
                return 'Inconsistent'
        elif float(df['col_177']) > float(df['col_175']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #12.1.2.b(178) <= 12.1.1.b(176)
    def res44(df):
        if pd.isnull(df['col_178']) and pd.isnull(df['col_176']):
            return 'Blank'
        elif pd.isnull(df['col_178']) or pd.isnull(df['col_176']):
            if pd.isnull(df['col_178']):
                return 'Probable Reporting Error(12.1.2.b is blank)'
            elif pd.isnull((float(df['col_176']))):
                return 'Inconsistent'
        elif float(df['col_178']) > float(df['col_176']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #12.1.3.a(179) <= 12.1.1.a(175)
    def res45(df):
        if pd.isnull(df['col_179']) and pd.isnull(df['col_175']):
            return 'Blank'
        elif pd.isnull(df['col_179']) or pd.isnull(df['col_175']):
            if pd.isnull(df['col_179']):
                return 'Probable Reporting Error(12.1.3.a is blank)'
            elif pd.isnull((float(df['col_175']))):
                return 'Inconsistent'
        elif float(df['col_179']) > float(df['col_175']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #12.1.3.b(180) <= 12.1.1.b(176)
    def res46(df):
        if pd.isnull(df['col_180']) and pd.isnull(df['col_176']):
            return 'Blank'
        elif pd.isnull(df['col_180']) or pd.isnull(df['col_176']):
            if pd.isnull(df['col_180']):
                return 'Probable Reporting Error(12.1.3.b is blank)'
            elif pd.isnull((float(df['col_176']))):
                return 'Inconsistent'
        elif float(df['col_180']) > float(df['col_176']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #14.2.1(192) +14.2.2(193) >= 14.1.1(183) +14.1.2(184) +14.1.3(185) +14.1.4(186) +14.1.5(187) +14.1.6(188) +14.1.7(189) +14.1.8(190) +14.1.9(191)
    def res47(df):
        if pd.isnull(df['col_192']) and pd.isnull(df['col_193']) and pd.isnull(df['col_183']) and pd.isnull(df['col_184']) and pd.isnull(df['col_185']) and pd.isnull(df['col_186']) and pd.isnull(df['col_187']) and pd.isnull(df['col_188']) and pd.isnull(df['col_189']) and pd.isnull(df['col_190']) and pd.isnull(df['col_191']):
            return 'Blank'
        elif pd.isnull(df['col_192']) or pd.isnull(df['col_193']) or pd.isnull(df['col_183']) or pd.isnull(df['col_184']) or pd.isnull(df['col_185']) or pd.isnull(df['col_186']) or pd.isnull(df['col_187']) or pd.isnull(df['col_188']) or pd.isnull(df['col_189']) or pd.isnull(df['col_190']) or pd.isnull(df['col_191']):
            if pd.isnull((float(df['col_192'])) + (float(df['col_193']))):
                return 'Inconsistent'
            elif pd.isnull(float(df['col_183']) + float(df['col_184']) + float(df['col_185'])+ float(df['col_186']) + float(df['col_187']) + float(df['col_188'])+ float(df['col_189']) + float(df['col_190']) + float(df['col_191'])):
                return 'Probable Reporting Error'
        elif (float(df['col_192']) + float(df['col_193'])) < (float(df['col_183']) + float(df['col_184']) + float(df['col_185'])
                                                                                            + float(df['col_186']) + float(df['col_187']) + float(df['col_188'])
                                                                                            + float(df['col_189']) + float(df['col_190']) + float(df['col_191'])):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #14.3.3(198) <= 14.3.1.a(194) +14.3.1.b(195) +14.3.2.a(196) +14.3.2.b(197)
    def res48(df):
        if pd.isnull(df['col_198']) and pd.isnull(df['col_194']) and pd.isnull(df['col_195']) and pd.isnull(df['col_196']) and pd.isnull(df['col_197']):
            return 'Blank'
        elif pd.isnull(df['col_198']) or pd.isnull(df['col_194']) or pd.isnull(df['col_195']) or pd.isnull(df['col_196']) or pd.isnull(df['col_197']):
            if pd.isnull(df['col_198']):
                return 'Probable Reporting Error(14.3.3 is blank)'
            elif pd.isnull((float(df['col_194'])) + (float(df['col_195'])) + (float(df['col_196'])) + (float(df['col_197']))):
                return 'Inconsistent'
        elif float(df['col_198']) > float(df['col_194']) + float(df['col_195']) + float(df['col_196']) + float(df['col_197']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #14.4.1(199) <=14.3.1.a(194) +14.3.1.b(195) +14.3.2.a(196) +14.3.2.b(197)
    def res49(df):
        if pd.isnull(df['col_199']) and pd.isnull(df['col_194']) and pd.isnull(df['col_195']) and pd.isnull(df['col_196']) and pd.isnull(df['col_197']):
            return 'Blank'
        elif pd.isnull(df['col_199']) or pd.isnull(df['col_194']) or pd.isnull(df['col_195']) or pd.isnull(df['col_196']) or pd.isnull(df['col_197']):
            if pd.isnull(df['col_199']):
                return 'Probable Reporting Error(14.4.1 is blank)'
            elif pd.isnull((float(df['col_194'])) + (float(df['col_195'])) + (float(df['col_196'])) + (float(df['col_197']))):
                return 'Inconsistent'
        elif float(df['col_199']) > float(df['col_194']) + float(df['col_195']) + float(df['col_196']) + float(df['col_197']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #14.4.2(200) <=14.3.1.a(194)+ 14.3.1.b(195) +14.3.2.a(196) +14.3.2.b(197)
    def res50(df):
        if pd.isnull(df['col_200']) and pd.isnull(df['col_194']) and pd.isnull(df['col_195']) and pd.isnull(df['col_196']) and pd.isnull(df['col_197']):
            return 'Blank'
        elif pd.isnull(df['col_200']) or pd.isnull(df['col_194']) or pd.isnull(df['col_195']) or pd.isnull(df['col_196']) or pd.isnull(df['col_197']):
            if pd.isnull(df['col_200']):
                return 'Probable Reporting Error(14.4.2 is blank)'
            elif pd.isnull((float(df['col_194'])) + (float(df['col_195'])) + (float(df['col_196'])) + (float(df['col_197']))):
                return 'Inconsistent'
        elif float(df['col_200']) > float(df['col_194']) + float(df['col_195']) + float(df['col_196']) + float(df['col_197']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #14.4.2 (200)<=14.3.1.a (194)+14.3.1.b (195)+14.3.2.a (196)+14.3.2.b (197)
    def res50(df):
        if pd.isnull(df['col_200']) and pd.isnull(df['col_194']) and pd.isnull(df['col_195']) and pd.isnull(df['col_196']) and pd.isnull(df['col_197']):
            return 'Blank'
        elif pd.isnull(df['col_200']) or pd.isnull(df['col_194']) or pd.isnull(df['col_195']) or pd.isnull(df['col_196']) or pd.isnull(df['col_197']):
            if pd.isnull(df['col_200']):
                return 'Probable Reporting Error(14.4.2 is blank)'
            elif pd.isnull((float(df['col_194'])) + (float(df['col_195'])) + (float(df['col_196'])) + (float(df['col_197']))):
                return 'Inconsistent'
        elif float(df['col_200']) > float(df['col_194']) + float(df['col_195']) + float(df['col_196']) + float(df['col_197']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    #14.4.3 (201)<=14.3.1.a (194)+14.3.1.b (195)+14.3.2.a (196)+14.3.2.b (197)
    def res51(df):
        if pd.isnull(df['col_201']) and pd.isnull(df['col_194']) and pd.isnull(df['col_195']) and pd.isnull(df['col_196']) and pd.isnull(df['col_197']):
            return 'Blank'
        elif pd.isnull(df['col_201']) or pd.isnull(df['col_194']) or pd.isnull(df['col_195']) or pd.isnull(df['col_196']) or pd.isnull(df['col_197']):
            if pd.isnull(df['col_201']):
                return 'Probable Reporting Error(14.4.3 is blank)'
            elif pd.isnull((float(df['col_194'])) + (float(df['col_195'])) + (float(df['col_196'])) + (float(df['col_197']))):
                return 'Inconsistent'
        elif float(df['col_201']) > float(df['col_194']) + float(df['col_195']) + float(df['col_196']) + float(df['col_197']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #14.4.4 (202)<=14.3.1.a (194)+14.3.1.b (195)+14.3.2.a (196)+14.3.2.b (197)
    def res52(df):
        if pd.isnull(df['col_202']) and pd.isnull(df['col_194']) and pd.isnull(df['col_195']) and pd.isnull(df['col_196']) and pd.isnull(df['col_197']):
            return 'Blank'
        elif pd.isnull(df['col_202']) or pd.isnull(df['col_194']) or pd.isnull(df['col_195']) or pd.isnull(df['col_196']) or pd.isnull(df['col_197']):
            if pd.isnull(df['col_202']):
                return 'Probable Reporting Error(14.4.4 is blank)'
            elif pd.isnull((float(df['col_194'])) + (float(df['col_195'])) + (float(df['col_196'])) + (float(df['col_197']))):
                return 'Inconsistent'
        elif float(df['col_202']) > float(df['col_194']) + float(df['col_195']) + float(df['col_196']) + float(df['col_197']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    #14.4.5 (203)<=14.3.1.a (194)+14.3.1.b (195)+14.3.2.a (196)+14.3.2.b (197)
    def res53(df):
        if pd.isnull(df['col_203']) and pd.isnull(df['col_194']) and pd.isnull(df['col_195']) and pd.isnull(df['col_196']) and pd.isnull(df['col_197']):
            return 'Blank'
        elif pd.isnull(df['col_203']) or pd.isnull(df['col_194']) or pd.isnull(df['col_195']) or pd.isnull(df['col_196']) or pd.isnull(df['col_197']):
            if pd.isnull(df['col_203']):
                return 'Probable Reporting Error(14.4.5 is blank)'
            elif pd.isnull((float(df['col_194'])) + (float(df['col_195'])) + (float(df['col_196'])) + (float(df['col_197']))):
                return 'Inconsistent'
        elif float(df['col_203']) > float(df['col_194']) + float(df['col_195']) + float(df['col_196']) + float(df['col_197']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
    
    #14.4.6 (204)<=14.3.1.a (194)+14.3.1.b (195)+14.3.2.a (196)+14.3.2.b (197)
    def res54(df):
        if pd.isnull(df['col_204']) and pd.isnull(df['col_194']) and pd.isnull(df['col_195']) and pd.isnull(df['col_196']) and pd.isnull(df['col_197']):
            return 'Blank'
        elif pd.isnull(df['col_204']) or pd.isnull(df['col_194']) or pd.isnull(df['col_195']) or pd.isnull(df['col_196']) or pd.isnull(df['col_197']):
            if pd.isnull(df['col_204']):
                return 'Probable Reporting Error(14.4.6 is blank)'
            elif pd.isnull((float(df['col_194'])) + (float(df['col_195'])) + (float(df['col_196'])) + (float(df['col_197']))):
                return 'Inconsistent'
        elif float(df['col_204']) > float(df['col_194']) + float(df['col_195']) + float(df['col_196']) + float(df['col_197']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df        
    
    #14.4.7 (205)<=14.3.1.a (194)+14.3.1.b (195)+14.3.2.a (196)+14.3.2.b (197)
    def res55(df):
        if pd.isnull(df['col_205']) and pd.isnull(df['col_194']) and pd.isnull(df['col_195']) and pd.isnull(df['col_196']) and pd.isnull(df['col_197']):
            return 'Blank'
        elif pd.isnull(df['col_205']) or pd.isnull(df['col_194']) or pd.isnull(df['col_195']) or pd.isnull(df['col_196']) or pd.isnull(df['col_197']):
            if pd.isnull(df['col_205']):
                return 'Probable Reporting Error(14.4.7 is blank)'
            elif pd.isnull((float(df['col_194'])) + (float(df['col_195'])) + (float(df['col_196'])) + (float(df['col_197']))):
                return 'Inconsistent'
        elif float(df['col_205']) > float(df['col_194']) + float(df['col_195']) + float(df['col_196']) + float(df['col_197']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df      
    
    #14.4.8 (206)<=14.3.1.a (194)+14.3.1.b (195)+14.3.2.a (196)+14.3.2.b (197)
    def res56(df):
        if pd.isnull(df['col_206']) and pd.isnull(df['col_194']) and pd.isnull(df['col_195']) and pd.isnull(df['col_196']) and pd.isnull(df['col_197']):
            return 'Blank'
        elif pd.isnull(df['col_206']) or pd.isnull(df['col_194']) or pd.isnull(df['col_195']) or pd.isnull(df['col_196']) or pd.isnull(df['col_197']):
            if pd.isnull(df['col_206']):
                return 'Probable Reporting Error(14.4.8 is blank)'
            elif pd.isnull((float(df['col_194'])) + (float(df['col_195'])) + (float(df['col_196'])) + (float(df['col_197']))):
                return 'Inconsistent'
        elif float(df['col_206']) > float(df['col_194']) + float(df['col_195']) + float(df['col_196']) + float(df['col_197']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df    

    #14.6.1(208) <= 14.5(207)
    def res57(df):
        if pd.isnull(df['col_208']) and pd.isnull(df['col_207']):
            return 'Blank'
        elif pd.isnull(df['col_208']) or pd.isnull(df['col_207']):
            if pd.isnull(df['col_208']):
                return 'Probable Reporting Error(14.6.1 is blank)'
            elif pd.isnull(float(df['col_207'])):
                return 'Inconsistent'
        elif float(df['col_208']) > float(df['col_207']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df        
    
    #14.6.2(209) <= 14.5(207)
    def res58(df):
        if pd.isnull(df['col_209']) and pd.isnull(df['col_207']):
            return 'Blank'
        elif pd.isnull(df['col_209']) or pd.isnull(df['col_207']):
            if pd.isnull(df['col_209']):
                return 'Probable Reporting Error(14.6.2 is blank)'
            elif pd.isnull(float(df['col_207'])):
                return 'Inconsistent'
        elif float(df['col_209']) > float(df['col_207']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df  

    #14.6.3(210) <= 14.5(207)
    def res59(df):
        if pd.isnull(df['col_210']) and pd.isnull(df['col_207']):
            return 'Blank'
        elif pd.isnull(df['col_210']) or pd.isnull(df['col_207']):
            if pd.isnull(df['col_210']):
                return 'Probable Reporting Error(14.6.3 is blank)'
            elif pd.isnull(float(df['col_207'])):
                return 'Inconsistent'
        elif float(df['col_210']) > float(df['col_207']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df  

    #14.6.4(211) <= 14.5(207)
    def res60(df):
        if pd.isnull(df['col_211']) and pd.isnull(df['col_207']):
            return 'Blank'
        elif pd.isnull(df['col_211']) or pd.isnull(df['col_207']):
            if pd.isnull(df['col_211']):
                return 'Probable Reporting Error(14.6.4 is blank)'
            elif pd.isnull(float(df['col_207'])):
                return 'Inconsistent'
        elif float(df['col_211']) > float(df['col_207']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df              
    
    #14.6.5(212) <= 14.5(207)
    def res61(df):
        if pd.isnull(df['col_212']) and pd.isnull(df['col_207']):
            return 'Blank'
        elif pd.isnull(df['col_212']) or pd.isnull(df['col_207']):
            if pd.isnull(df['col_212']):
                return 'Probable Reporting Error(14.6.5 is blank)'
            elif pd.isnull(float(df['col_207'])):
                return 'Inconsistent'
        elif float(df['col_212']) > float(df['col_207']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df  

    #14.7(214) <= 14.5(207)
    def res62(df):
        if pd.isnull(df['col_214']) and pd.isnull(df['col_207']):
            return 'Blank'
        elif pd.isnull(df['col_214']) or pd.isnull(df['col_207']):
            if pd.isnull(df['col_214']):
                return 'Probable Reporting Error(14.7 is blank)'
            elif pd.isnull(float(df['col_207'])):
                return 'Inconsistent'
        elif float(df['col_214']) > float(df['col_207']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df  

    #14.14.2(231) <= 14.14.1(230)
    def res63(df):
        if pd.isnull(df['col_231']) and pd.isnull(df['col_230']):
            return 'Blank'
        elif pd.isnull(df['col_231']) or pd.isnull(df['col_230']):
            if pd.isnull(df['col_231']):
                return 'Probable Reporting Error(14.14.2 is blank)'
            elif pd.isnull(float(df['col_230'])):
                return 'Inconsistent'
        elif float(df['col_231']) > float(df['col_230']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    #15.2.2(235) <= 15.2.1(234)
    def res64(df):
        if pd.isnull(df['col_235']) and pd.isnull(df['col_234']):
            return 'Blank'
        elif pd.isnull(df['col_235']) or pd.isnull(df['col_234']):
            if pd.isnull(df['col_235']):
                return 'Probable Reporting Error(15.2.2 is blank)'
            elif pd.isnull(float(df['col_234'])):
                return 'Inconsistent'
        elif float(df['col_235']) > float(df['col_234']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    #15.3.2b(240) <= 15.3.2a(239)
    def res65(df):
        if pd.isnull(df['col_240']) and pd.isnull(df['col_239']):
            return 'Blank'
        elif pd.isnull(df['col_240']) or pd.isnull(df['col_239']):
            if pd.isnull(df['col_240']):
                return 'Probable Reporting Error(15.3.2b is blank)'
            elif pd.isnull(float(df['col_239'])):
                return 'Inconsistent'
        elif float(df['col_240']) > float(df['col_239']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    #15.3.3b(241) <= 15.3.3a(240)
    def res66(df):
        if pd.isnull(df['col_241']) and pd.isnull(df['col_240']):
            return 'Blank'
        elif pd.isnull(df['col_241']) or pd.isnull(df['col_240']):
            if pd.isnull(df['col_241']):
                return 'Probable Reporting Error(15.3.3b is blank)'
            elif pd.isnull(float(df['col_240'])):
                return 'Inconsistent'
        elif float(df['col_241']) > float(df['col_240']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    #15.3.3c(242) <= 15.3.3b(241)
    def res67(df):
        if pd.isnull(df['col_242']) and pd.isnull(df['col_241']):
            return 'Blank'
        elif pd.isnull(df['col_242']) or pd.isnull(df['col_241']):
            if pd.isnull(df['col_242']):
                return 'Probable Reporting Error(15.3.3c is blank)'
            elif pd.isnull(float(df['col_241'])):
                return 'Inconsistent'
        elif float(df['col_242']) > float(df['col_241']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    #15.4.2(248) <= 15.4.1(247)
    def res68(df):
        if pd.isnull(df['col_248']) and pd.isnull(df['col_247']):
            return 'Blank'
        elif pd.isnull(df['col_248']) or pd.isnull(df['col_247']):
            if pd.isnull(df['col_250']):
                return 'Probable Reporting Error(15.4.2 is blank)'
            elif pd.isnull(float(df['col_247'])):
                return 'Inconsistent'
        elif float(df['col_248']) > float(df['col_247']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    #9.6.1 (139) <=9.1.1 (100)+9.1.2 (101)+9.1.3 (102)+9.1.4 (103)+9.1.5 (104)+9.1.6 (105)+9.1.7 (106)+9.1.8 (107)+9.1.13 (112)+9.1.14 (113)+9.1.15 (114)+9.1.16 (115)+9.1.17 (116)+9.1.18 (117)+9.1.19 (118)+9.1.20 (119)+9.1.21 (120)+9.2.1 (121)+9.2.2 (122)+9.2.3 (123)+9.3.1 (126)+9.3.2 (127)+9.3.3 (128)+9.4.1 (129)+9.4.2 (130)+9.4.3 (131)+9.4.5 (133)+9.4.6 (134)+9.5.1 (135)+9.5.2 (136)+9.5.3 (137)+9.5.4 (138)
    def res69(df):
        if pd.isnull(df['col_139']) and pd.isnull(df['col_100']) and pd.isnull(df['col_101']) and pd.isnull(df['col_102']) and pd.isnull(df['col_103']) and pd.isnull(df['col_104']) and pd.isnull(df['col_105']) and pd.isnull(df['col_106']) and pd.isnull(df['col_107']) and pd.isnull(df['col_112']) and pd.isnull(df['col_113']) and pd.isnull(df['col_114']) and pd.isnull(df['col_115']) and pd.isnull(df['col_116']) and pd.isnull(df['col_117']) and pd.isnull(df['col_118']) and pd.isnull(df['col_119']) and pd.isnull(df['col_120']) and pd.isnull(df['col_121']) and pd.isnull(df['col_122']) and pd.isnull(df['col_123']) and pd.isnull(df['col_126']) and pd.isnull(df['col_127']) and pd.isnull(df['col_128']) and pd.isnull(df['col_129']) and pd.isnull(df['col_130']) and pd.isnull(df['col_131']) and pd.isnull(df['col_133']) and pd.isnull(df['col_134']) and pd.isnull(df['col_135']) and pd.isnull(df['col_136']) and pd.isnull(df['col_137']) and pd.isnull(df['col_138']):
            return 'Blank'
        elif pd.isnull(df['col_139']) or pd.isnull(df['col_100']) or pd.isnull(df['col_101']) or pd.isnull(df['col_102']) or pd.isnull(df['col_103']) or pd.isnull(df['col_104']) or pd.isnull(df['col_105']) or pd.isnull(df['col_106']) or pd.isnull(df['col_107']) or pd.isnull(df['col_112']) or pd.isnull(df['col_113']) or pd.isnull(df['col_114']) or pd.isnull(df['col_115']) or pd.isnull(df['col_116']) or pd.isnull(df['col_117']) or pd.isnull(df['col_118']) or pd.isnull(df['col_119']) or pd.isnull(df['col_120']) or pd.isnull(df['col_121']) or pd.isnull(df['col_122']) or pd.isnull(df['col_123']) or pd.isnull(df['col_126']) or pd.isnull(df['col_127']) or pd.isnull(df['col_128']) or pd.isnull(df['col_129']) or pd.isnull(df['col_130']) or pd.isnull(df['col_131']) or pd.isnull(df['col_133']) or pd.isnull(df['col_134']) or pd.isnull(df['col_135']) or pd.isnull(df['col_136']) or pd.isnull(df['col_137']) or pd.isnull(df['col_138']):
            if pd.isnull(df['col_139']):
                return 'Probable Reporting Error(9.6.1 is blank)'
            elif pd.isnull((float(df['col_100'])) + (float(df['col_101'])) + (float(df['col_102'])) + (float(df['col_103'])) + (float(df['col_104'])) + (float(df['col_105'])) + (float(df['col_106'])) + (float(df['col_107'])) + (float(df['col_112'])) + (float(df['col_113'])) + (float(df['col_114'])) + (float(df['col_115'])) + (float(df['col_116'])) + (float(df['col_117'])) + (float(df['col_118'])) + (float(df['col_119'])) + (float(df['col_120'])) + (float(df['col_121'])) + (float(df['col_122'])) + (float(df['col_123'])) + (float(df['col_126'])) + (float(df['col_127'])) + (float(df['col_128'])) + (float(df['col_129'])) + (float(df['col_130'])) + (float(df['col_131'])) + (float(df['col_133'])) + (float(df['col_134'])) + (float(df['col_135'])) + (float(df['col_136'])) + (float(df['col_137'])) + (float(df['col_138']))):
                return 'Inconsistent'
        elif float(df['col_139']) > float(df['col_100']) > + (float(df['col_101']) + float(df['col_102']) + float(df['col_103']) + float(df['col_104']) + float(df['col_105']) + float(df['col_106']) + float(df['col_107']) + float(df['col_112']) + float(df['col_113']) + float(df['col_114']) + float(df['col_115']) + float(df['col_116']) + float(df['col_117']) + float(df['col_118']) + float(df['col_119']) + float(df['col_120']) + float(df['col_121']) + float(df['col_122']) + float(df['col_123']) + float(df['col_126']) + float(df['col_127']) + float(df['col_128']) + float(df['col_129']) + float(df['col_130']) + float(df['col_131']) + float(df['col_133']) + float(df['col_134']) + float(df['col_135']) + float(df['col_136']) + float(df['col_137']) + float(df['col_138'])):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df  

    #9.6.2 (140) <=9.1.1 (100)+9.1.2 (101)+9.1.3 (102)+9.1.4 (103)+9.1.5 (104)+9.1.6 (105)+9.1.7 (106)+9.1.8 (107)+9.1.13 (112)+9.1.14 (113)+9.1.15 (114)+9.1.16 (115)+9.1.17 (116)+9.1.18 (117)+9.1.19 (118)+9.1.20 (119)+9.1.21 (120)+9.2.1 (121)+9.2.2 (122)+9.2.3 (123)+9.3.1 (126)+9.3.2 (127)+9.3.3 (128)+9.4.1 (129)+9.4.2 (130)+9.4.3 (131)+9.4.5 (133)+9.4.6 (134)+9.5.1 (135)+9.5.2 (136)+9.5.3 (137)+9.5.4 (138)
    def res70(df):
        if pd.isnull(df['col_140']) and pd.isnull(df['col_100']) and pd.isnull(df['col_101']) and pd.isnull(df['col_102']) and pd.isnull(df['col_103']) and pd.isnull(df['col_104']) and pd.isnull(df['col_105']) and pd.isnull(df['col_106']) and pd.isnull(df['col_107']) and pd.isnull(df['col_112']) and pd.isnull(df['col_113']) and pd.isnull(df['col_114']) and pd.isnull(df['col_115']) and pd.isnull(df['col_116']) and pd.isnull(df['col_117']) and pd.isnull(df['col_118']) and pd.isnull(df['col_119']) and pd.isnull(df['col_120']) and pd.isnull(df['col_121']) and pd.isnull(df['col_122']) and pd.isnull(df['col_123']) and pd.isnull(df['col_126']) and pd.isnull(df['col_127']) and pd.isnull(df['col_128']) and pd.isnull(df['col_129']) and pd.isnull(df['col_130']) and pd.isnull(df['col_131']) and pd.isnull(df['col_133']) and pd.isnull(df['col_134']) and pd.isnull(df['col_135']) and pd.isnull(df['col_136']) and pd.isnull(df['col_137']) and pd.isnull(df['col_138']):
            return 'Blank'
        elif pd.isnull(df['col_140']) or pd.isnull(df['col_100']) or pd.isnull(df['col_101']) or pd.isnull(df['col_102']) or pd.isnull(df['col_103']) or pd.isnull(df['col_104']) or pd.isnull(df['col_105']) or pd.isnull(df['col_106']) or pd.isnull(df['col_107']) or pd.isnull(df['col_112']) or pd.isnull(df['col_113']) or pd.isnull(df['col_114']) or pd.isnull(df['col_115']) or pd.isnull(df['col_116']) or pd.isnull(df['col_117']) or pd.isnull(df['col_118']) or pd.isnull(df['col_119']) or pd.isnull(df['col_120']) or pd.isnull(df['col_121']) or pd.isnull(df['col_122']) or pd.isnull(df['col_123']) or pd.isnull(df['col_126']) or pd.isnull(df['col_127']) or pd.isnull(df['col_128']) or pd.isnull(df['col_129']) or pd.isnull(df['col_130']) or pd.isnull(df['col_131']) or pd.isnull(df['col_133']) or pd.isnull(df['col_134']) or pd.isnull(df['col_135']) or pd.isnull(df['col_136']) or pd.isnull(df['col_137']) or pd.isnull(df['col_138']):
            if pd.isnull(df['col_140']):
                return 'Probable Reporting Error(9.6.2 is blank)'
            elif pd.isnull((float(df['col_100'])) + (float(df['col_101'])) + (float(df['col_102'])) + (float(df['col_103'])) + (float(df['col_104'])) + (float(df['col_105'])) + (float(df['col_106'])) + (float(df['col_107'])) + (float(df['col_112'])) + (float(df['col_113'])) + (float(df['col_114'])) + (float(df['col_115'])) + (float(df['col_116'])) + (float(df['col_117'])) + (float(df['col_118'])) + (float(df['col_119'])) + (float(df['col_120'])) + (float(df['col_121'])) + (float(df['col_122'])) + (float(df['col_123'])) + (float(df['col_126'])) + (float(df['col_127'])) + (float(df['col_128'])) + (float(df['col_129'])) + (float(df['col_130'])) + (float(df['col_131'])) + (float(df['col_133'])) + (float(df['col_134'])) + (float(df['col_135'])) + (float(df['col_136'])) + (float(df['col_137'])) + (float(df['col_138']))):
                return 'Inconsistent'
        elif float(df['col_140']) > float(df['col_100']) > + (float(df['col_101']) + float(df['col_102']) + float(df['col_103']) + float(df['col_104']) + float(df['col_105']) + float(df['col_106']) + float(df['col_107']) + float(df['col_112']) + float(df['col_113']) + float(df['col_114']) + float(df['col_115']) + float(df['col_116']) + float(df['col_117']) + float(df['col_118']) + float(df['col_119']) + float(df['col_120']) + float(df['col_121']) + float(df['col_122']) + float(df['col_123']) + float(df['col_126']) + float(df['col_127']) + float(df['col_128']) + float(df['col_129']) + float(df['col_130']) + float(df['col_131']) + float(df['col_133']) + float(df['col_134']) + float(df['col_135']) + float(df['col_136']) + float(df['col_137']) + float(df['col_138'])):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df  

    #9.6.3 (141) <=9.1.1 (100)+9.1.2 (101)+9.1.3 (102)+9.1.4 (103)+9.1.5 (104)+9.1.6 (105)+9.1.7 (106)+9.1.8 (107)+9.1.13 (112)+9.1.14 (113)+9.1.15 (114)+9.1.16 (115)+9.1.17 (116)+9.1.18 (117)+9.1.19 (118)+9.1.20 (119)+9.1.21 (120)+9.2.1 (121)+9.2.2 (122)+9.2.3 (123)+9.3.1 (126)+9.3.2 (127)+9.3.3 (128)+9.4.1 (129)+9.4.2 (130)+9.4.3 (131)+9.4.5 (133)+9.4.6 (134)+9.5.1 (135)+9.5.2 (136)+9.5.3 (137)+9.5.4 (138)
    def res71(df):
        if pd.isnull(df['col_141']) and pd.isnull(df['col_100']) and pd.isnull(df['col_101']) and pd.isnull(df['col_102']) and pd.isnull(df['col_103']) and pd.isnull(df['col_104']) and pd.isnull(df['col_105']) and pd.isnull(df['col_106']) and pd.isnull(df['col_107']) and pd.isnull(df['col_112']) and pd.isnull(df['col_113']) and pd.isnull(df['col_114']) and pd.isnull(df['col_115']) and pd.isnull(df['col_116']) and pd.isnull(df['col_117']) and pd.isnull(df['col_118']) and pd.isnull(df['col_119']) and pd.isnull(df['col_120']) and pd.isnull(df['col_121']) and pd.isnull(df['col_122']) and pd.isnull(df['col_123']) and pd.isnull(df['col_126']) and pd.isnull(df['col_127']) and pd.isnull(df['col_128']) and pd.isnull(df['col_129']) and pd.isnull(df['col_130']) and pd.isnull(df['col_131']) and pd.isnull(df['col_133']) and pd.isnull(df['col_134']) and pd.isnull(df['col_135']) and pd.isnull(df['col_136']) and pd.isnull(df['col_137']) and pd.isnull(df['col_138']):
            return 'Blank'
        elif pd.isnull(df['col_141']) or pd.isnull(df['col_100']) or pd.isnull(df['col_101']) or pd.isnull(df['col_102']) or pd.isnull(df['col_103']) or pd.isnull(df['col_104']) or pd.isnull(df['col_105']) or pd.isnull(df['col_106']) or pd.isnull(df['col_107']) or pd.isnull(df['col_112']) or pd.isnull(df['col_113']) or pd.isnull(df['col_114']) or pd.isnull(df['col_115']) or pd.isnull(df['col_116']) or pd.isnull(df['col_117']) or pd.isnull(df['col_118']) or pd.isnull(df['col_119']) or pd.isnull(df['col_120']) or pd.isnull(df['col_121']) or pd.isnull(df['col_122']) or pd.isnull(df['col_123']) or pd.isnull(df['col_126']) or pd.isnull(df['col_127']) or pd.isnull(df['col_128']) or pd.isnull(df['col_129']) or pd.isnull(df['col_130']) or pd.isnull(df['col_131']) or pd.isnull(df['col_133']) or pd.isnull(df['col_134']) or pd.isnull(df['col_135']) or pd.isnull(df['col_136']) or pd.isnull(df['col_137']) or pd.isnull(df['col_138']):
            if pd.isnull(df['col_141']):
                return 'Probable Reporting Error(9.6.3 is blank)'
            elif pd.isnull((float(df['col_100'])) + (float(df['col_101'])) + (float(df['col_102'])) + (float(df['col_103'])) + (float(df['col_104'])) + (float(df['col_105'])) + (float(df['col_106'])) + (float(df['col_107'])) + (float(df['col_112'])) + (float(df['col_113'])) + (float(df['col_114'])) + (float(df['col_115'])) + (float(df['col_116'])) + (float(df['col_117'])) + (float(df['col_118'])) + (float(df['col_119'])) + (float(df['col_120'])) + (float(df['col_121'])) + (float(df['col_122'])) + (float(df['col_123'])) + (float(df['col_126'])) + (float(df['col_127'])) + (float(df['col_128'])) + (float(df['col_129'])) + (float(df['col_130'])) + (float(df['col_131'])) + (float(df['col_133'])) + (float(df['col_134'])) + (float(df['col_135'])) + (float(df['col_136'])) + (float(df['col_137'])) + (float(df['col_138']))):
                return 'Inconsistent'
        elif float(df['col_141']) > float(df['col_100']) > + (float(df['col_101']) + float(df['col_102']) + float(df['col_103']) + float(df['col_104']) + float(df['col_105']) + float(df['col_106']) + float(df['col_107']) + float(df['col_112']) + float(df['col_113']) + float(df['col_114']) + float(df['col_115']) + float(df['col_116']) + float(df['col_117']) + float(df['col_118']) + float(df['col_119']) + float(df['col_120']) + float(df['col_121']) + float(df['col_122']) + float(df['col_123']) + float(df['col_126']) + float(df['col_127']) + float(df['col_128']) + float(df['col_129']) + float(df['col_130']) + float(df['col_131']) + float(df['col_133']) + float(df['col_134']) + float(df['col_135']) + float(df['col_136']) + float(df['col_137']) + float(df['col_138'])):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df 

    #9.7.2(143) <= 9.7.1(142)
    def res72(df):
        if pd.isnull(df['col_143']) and pd.isnull(df['col_142']):
            return 'Blank'
        elif pd.isnull(df['col_143']) or pd.isnull(df['col_142']):
            if pd.isnull(df['col_143']):
                return 'Probable Reporting Error(9.7.2 is blank)'
            elif pd.isnull(float(df['col_142'])):
                return 'Inconsistent'
        elif float(df['col_143']) > float(df['col_142']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    #9.7.3(144) <= 9.7.2(143)
    def res73(df):
        if pd.isnull(df['col_144']) and pd.isnull(df['col_143']):
            return 'Blank'
        elif pd.isnull(df['col_144']) or pd.isnull(df['col_143']):
            if pd.isnull(df['col_144']):
                return 'Probable Reporting Error(9.7.3 is blank)'
            elif pd.isnull(float(df['col_143'])):
                return 'Inconsistent'
        elif float(df['col_144']) > float(df['col_143']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    #11.1.1b (166) <= 11.1.1a (165)
    def res74(df):
        if pd.isnull(df['col_166']) and pd.isnull(df['col_165']):
            return 'Blank'
        elif pd.isnull(df['col_166']) or pd.isnull(df['col_165']):
            if pd.isnull(df['col_166']):
                return 'Probable Reporting Error(11.1.1b is blank)'
            elif pd.isnull(float(df['col_165'])):
                return 'Inconsistent'
        elif float(df['col_166']) > float(df['col_165']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    #11.1.1c (167) <= 11.1.1a (165)
    def res75(df):
        if pd.isnull(df['col_167']) and pd.isnull(df['col_165']):
            return 'Blank'
        elif pd.isnull(df['col_167']) or pd.isnull(df['col_165']):
            if pd.isnull(df['col_167']):
                return 'Probable Reporting Error(11.1.1c is blank)'
            elif pd.isnull(float(df['col_165'])):
                return 'Inconsistent'
        elif float(df['col_167']) > float(df['col_165']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    #11.1.2b (169) <= 11.1.2a (168)
    def res76(df):
        if pd.isnull(df['col_169']) and pd.isnull(df['col_168']):
            return 'Blank'
        elif pd.isnull(df['col_169']) or pd.isnull(df['col_168']):
            if pd.isnull(df['col_169']):
                return 'Probable Reporting Error(11.1.2b is blank)'
            elif pd.isnull(float(df['col_168'])):
                return 'Inconsistent'
        elif float(df['col_169']) > float(df['col_168']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df

    #11.1.2c (170) <= 11.1.2a (168)
    def res77(df):
        if pd.isnull(df['col_170']) and pd.isnull(df['col_168']):
            return 'Blank'
        elif pd.isnull(df['col_170']) or pd.isnull(df['col_168']):
            if pd.isnull(df['col_170']):
                return 'Probable Reporting Error(11.1.2c is blank)'
            elif pd.isnull(float(df['col_170'])):
                return 'Inconsistent'
        elif float(df['col_170']) > float(df['col_168']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df     
    
    #14.9.1 (220)<=14.3.1.a (194)+14.3.1.b (195)
    def res78(df):
        if pd.isnull(df['col_220']) and pd.isnull(df['col_194']) and pd.isnull(df['col_195']):
            return 'Blank'
        elif pd.isnull(df['col_220']) or pd.isnull(df['col_194']) or pd.isnull(df['col_195']):
            if pd.isnull(df['col_220']):
                return 'Probable Reporting Error(14.9.1 is blank)'
            elif pd.isnull((float(df['col_194'])) + (float(df['col_195']))):
                return 'Inconsistent'
        elif float(df['col_220']) > float(df['col_194']) + float(df['col_195']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df      

    #14.9.2 (221)<=14.3.2.a (196)+14.3.2.b (197)
    def res79(df):
        if pd.isnull(df['col_221']) and pd.isnull(df['col_196']) and pd.isnull(df['col_197']):
            return 'Blank'
        elif pd.isnull(df['col_221']) or pd.isnull(df['col_196']) or pd.isnull(df['col_197']):
            if pd.isnull(df['col_221']):
                return 'Probable Reporting Error(14.9.2 is blank)'
            elif pd.isnull((float(df['col_196'])) + (float(df['col_197']))):
                return 'Inconsistent'
        elif float(df['col_221']) > float(df['col_196']) + float(df['col_197']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df     

    #14.13 (229)<=14.12.1 (224)+14.12.2 (225)+14.12.3 (226)+14.12.4 (227)+14.12.5 (228)
    def res80(df):
        if pd.isnull(df['col_229']) and pd.isnull(df['col_224']) and pd.isnull(df['col_225']) and pd.isnull(df['col_226']) and pd.isnull(df['col_227']) and pd.isnull(df['col_228']):
            return 'Blank'
        elif pd.isnull(df['col_229']) or pd.isnull(df['col_224']) or pd.isnull(df['col_225']) or pd.isnull(df['col_226']) or pd.isnull(df['col_227']) or pd.isnull(df['col_228']):
            if pd.isnull(df['col_229']):
                return 'Probable Reporting Error(14.13 is blank)'
            elif pd.isnull((float(df['col_224'])) + (float(df['col_225'])) + (float(df['col_226'])) + (float(df['col_227'])) + (float(df['col_228']))):
                return 'Inconsistent'
        elif float(df['col_229']) > float(df['col_224']) + float(df['col_225']) + float(df['col_226']) + float(df['col_227']) + float(df['col_228']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df      

    #14.8.2(216) <= 14.8.1(215)
    def res81(df):
        if pd.isnull(df['col_216']) and pd.isnull(df['col_215']):
            return 'Blank'
        elif pd.isnull(df['col_216']) or pd.isnull(df['col_215']):
            if pd.isnull(df['col_216']):
                return 'Probable Reporting Error(14.8.2 is blank)'
            elif pd.isnull(float(df['col_215'])):
                return 'Inconsistent'
        elif float(df['col_216']) > float(df['col_215']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df
            
    #15.3.4b(244) <= 15.3.4a(243)
    def res82(df):
        if pd.isnull(df['col_244']) and pd.isnull(df['col_243']):
            return 'Blank'
        elif pd.isnull(df['col_244']) or pd.isnull(df['col_243']):
            if pd.isnull(df['col_244']):
                return 'Probable Reporting Error(15.3.4b is blank)'
            elif pd.isnull(float(df['col_243'])):
                return 'Inconsistent'
        elif float(df['col_244']) > float(df['col_243']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df       

    #15.3.4d(246) <= 15.3.4c(245)
    def res83(df):
        if pd.isnull(df['col_246']) and pd.isnull(df['col_245']):
            return 'Blank'
        elif pd.isnull(df['col_246']) or pd.isnull(df['col_245']):
            if pd.isnull(df['col_246']):
                return 'Probable Reporting Error(15.3.4d is blank)'
            elif pd.isnull(float(df['col_245'])):
                return 'Inconsistent'
        elif float(df['col_246']) > float(df['col_245']):
            return 'Inconsistent'
        else:
            return 'consistent'
        return df 

    # Renaming column names===============================CHC


    df['1.1.1<=1.1'] = df.apply(res1, axis=1)
    df['15.3.1.b<=15.3.1.a'] = df.apply(res2, axis=1)
    df['1.2.4<=1.1'] = df.apply(res3, axis=1)
    df['1.2.5<=1.1'] = df.apply(res4, axis=1)
    df['1.2.7<=1.1'] = df.apply(res5, axis=1)
    df['1.3.1.a<=1.3.1'] = df.apply(res6, axis=1)
    df['1.3.2<=2.1'] = df.apply(res7, axis=1)
    df['1.4.4>=1.4.3'] = df.apply(res8, axis=1)
    df['1.5.2<=1.5.1'] = df.apply(res9, axis=1)
    df['1.5.1<=1.1'] = df.apply(res10, axis=1)
    df['1.5.3<=1.5.2'] = df.apply(res11, axis=1)
    df['1.6.1.b<=1.6.1.a'] = df.apply(res12, axis=1)
    df['1.6.1.a<=1.1'] = df.apply(res13, axis=1)
    df['1.6.1.c<=1.6.1.b'] = df.apply(res14, axis=1)
    df['1.6.1.e<=1.6.1.d'] = df.apply(res15, axis=1)
    df['2.1.1<=2.1'] = df.apply(res16, axis=1)
    df['3.1<=2.1'] = df.apply(res17, axis=1)
    df['3.1.1<=3.1'] = df.apply(res18, axis=1)
    df['4.1.1.a+4.1.1.b+4.1.3>=2.1'] = df.apply(res19, axis=1)
    df['4.1.2<=4.1.1.a+4.1.1.b'] = df.apply(res20, axis=1)
    df['4.3.2.a<=4.3.1.a+4.3.1.b+4.2'] = df.apply(res21, axis=1)
    df['4.3.2.b<=4.3.2.a'] = df.apply(res22, axis=1)
    df['4.3.3<=4.3.1.a+4.3.1.b+4.2'] = df.apply(res23, axis=1)
    df['4.4.1<=4.1.1.a+4.1.1.b'] = df.apply(res24, axis=1)
    df['4.4.2<=4.4.1'] = df.apply(res25, axis=1)
    df['4.4.3<=4.1.1.a+4.1.1.b'] = df.apply(res26, axis=1)
    df['5.2<=5.1'] = df.apply(res27, axis=1)
    df['6.3<=2.1'] = df.apply(res28, axis=1)
    df['6.4<=2.1'] = df.apply(res29, axis=1)
    df['7.2.1<=7.1.1'] = df.apply(res30, axis=1)
    df['7.2.2<=7.1.2'] = df.apply(res31, axis=1)
    df['8.2.3<=2.1'] = df.apply(res32, axis=1)
    df['8.4<=2.1'] = df.apply(res33, axis=1)
    df['8.7<=8.3+8.4+8.5'] = df.apply(res34, axis=1)
    df['8.17.1<=8.1.1'] = df.apply(res35, axis=1)
    df['8.17.2<=8.2.1+8.2.2+8.2.3+8.2.4'] = df.apply(res36, axis=1)
    df['9.1.1<=4.1.1.a+4.1.1.b'] = df.apply(res37, axis=1)
    df['9.1.2<=4.1.1.a+4.1.1.b'] = df.apply(res38, axis=1)
    df['9.1.9<=4.1.1.a+4.1.1.b'] = df.apply(res39, axis=1)
    df['9.1.13<=4.1.1.a+4.1.1.b'] = df.apply(res40, axis=1)
    df['9.2.4.a+9.2.4.b<=9.2.1+ 9.2.2'] = df.apply(res41, axis=1)
    df['11.2.2<=11.2.1'] = df.apply(res42, axis=1)
    df['12.1.2.a<=12.1.1.a'] = df.apply(res43, axis=1)
    df['12.1.2.b<=12.1.1.b'] = df.apply(res44, axis=1)
    df['12.1.3.a<=12.1.1.a'] = df.apply(res45, axis=1)
    df['12.1.3.b<=12.1.1.b'] = df.apply(res46, axis=1)
    df['14.2.1+14.2.2>=14.1.1+14.1.2+14.1.3+14.1.4+14.1.5+14.1.6+14.1.7+14.1.8+14.1.9'] = df.apply(res47, axis=1)
    df['14.3.3<=14.3.1.a+14.3.1.b+14.3.2.a+14.3.2.b'] = df.apply(res48, axis=1)
    df['14.4.1<=14.3.1.a+14.3.1.b+14.3.2.a+14.3.2.b'] = df.apply(res49, axis=1)
    df['14.4.2<=14.3.1.a+14.3.1.b+14.3.2.a+14.3.2.b'] = df.apply(res50, axis=1)
    df['14.4.3<=14.3.1.a+14.3.1.b+14.3.2.a+14.3.2.b'] = df.apply(res51, axis=1)
    df['14.4.4<=14.3.1.a+14.3.1.b+14.3.2.a+14.3.2.b'] = df.apply(res52, axis=1)
    df['14.4.5<=14.3.1.a+14.3.1.b+14.3.2.a+14.3.2.b'] = df.apply(res53, axis=1)
    df['14.4.6<=14.3.1.a+14.3.1.b+14.3.2.a+14.3.2.b'] = df.apply(res54, axis=1)
    df['14.4.7<=14.3.1.a+14.3.1.b+14.3.2.a+14.3.2.b'] = df.apply(res55, axis=1)
    df['14.4.8<=14.3.1.a+14.3.1.b+14.3.2.a+14.3.2.b'] = df.apply(res56, axis=1)
    df['14.6.1<=14.5'] = df.apply(res57, axis=1)
    df['14.6.2<=14.5'] = df.apply(res58, axis=1)
    df['14.6.3<=14.5'] = df.apply(res59, axis=1)
    df['14.6.4<=14.5'] = df.apply(res60, axis=1)
    df['14.6.5<=14.5'] = df.apply(res61, axis=1)
    df['14.7<=14.5'] = df.apply(res62, axis=1)
    df['14.14.2<=14.14.1'] = df.apply(res63, axis=1)
    df['15.2.2<=15.2.1'] = df.apply(res64, axis=1)
    df['15.3.2.b<=15.3.2.a'] = df.apply(res65, axis=1)
    df['15.3.3.b<=15.3.3.a'] = df.apply(res66, axis=1)
    df['15.3.3.c<=15.3.3.b'] = df.apply(res67, axis=1)
    df['15.4.2<=15.4.1'] = df.apply(res68, axis=1)
    df['9.6.1<=9.1.1+9.1.2+9.1.3+9.1.4+9.1.5+9.1.6+9.1.7+9.1.8+9.1.13+9.1.14+9.1.15+9.1.16+9.1.17+9.1.18+9.1.19+9.1.20+9.1.21+9.2.1+9.2.2+9.2.3+9.3.1+9.3.2+9.3.3+9.4.1+9.4.2+9.4.3+9.4.5+9.4.6+9.5.1+9.5.2+9.5.3+9.5.4'] = df.apply(res69, axis=1)
    df['9.6.2<=9.1.1+9.1.2+9.1.3+9.1.4+9.1.5+9.1.6+9.1.7+9.1.8+9.1.13+9.1.14+9.1.15+9.1.16+9.1.17+9.1.18+9.1.19+9.1.20+9.1.21+9.2.1+9.2.2+9.2.3+9.3.1+9.3.2+9.3.3+9.4.1+9.4.2+9.4.3+9.4.5+9.4.6+9.5.1+9.5.2+9.5.3+9.5.4'] = df.apply(res70, axis=1)
    df['9.6.3<=9.1.1+9.1.2+9.1.3+9.1.4+9.1.5+9.1.6+9.1.7+9.1.8+9.1.13+9.1.14+9.1.15+9.1.16+9.1.17+9.1.18+9.1.19+9.1.20+9.1.21+9.2.1+9.2.2+9.2.3+9.3.1+9.3.2+9.3.3+9.4.1+9.4.2+9.4.3+9.4.5+9.4.6+9.5.1+9.5.2+9.5.3+9.5.4'] = df.apply(res71, axis=1)
    df['9.7.2<=9.7.1'] = df.apply(res72, axis=1)
    df['9.7.3<=9.7.2'] = df.apply(res73, axis=1)
    df['11.1.1.b<=11.1.1.a'] = df.apply(res74, axis=1)
    df['11.1.1.c<=11.1.1.a'] = df.apply(res75, axis=1)
    df['11.1.2.b<=11.1.2.a'] = df.apply(res76, axis=1)
    df['11.1.2.c<=11.1.2.a'] = df.apply(res77, axis=1)
    df['14.9.1<=14.3.1.a+14.3.1.b'] = df.apply(res78, axis=1)
    df['14.9.2<=14.3.2.a+14.3.2.b'] = df.apply(res79, axis=1)
    df['14.13<=14.12.1+14.12.2+14.12.3+14.12.4+14.12.5'] = df.apply(res80, axis=1)
    df['14.8.2<=14.8.1'] = df.apply(res81, axis=1)
    df['15.3.4.b<=15.3.4.a'] = df.apply(res82, axis=1)
    df['15.3.4.d<=15.3.4.c'] = df.apply(res83, axis=1)


    # Merging all the renamed columns
    # ===============================
    df= pd.concat ([df ['1.1.1<=1.1'],
                    df ['15.3.1.b<=15.3.1.a'],
                    df ['1.2.4<=1.1'],
                    df ['1.2.5<=1.1'],
                    df ['1.2.7<=1.1'],
                    df ['1.3.1.a<=1.3.1'],
                    df ['1.3.2<=2.1'],
                    df ['1.4.4>=1.4.3'],
                    df ['1.5.2<=1.5.1'],
                        df ['1.5.1<=1.1'],
                        df ['1.5.3<=1.5.2'],
                        df ['1.6.1.b<=1.6.1.a'],
                        df ['1.6.1.a<=1.1'],
                        df ['1.6.1.c<=1.6.1.b'],
                        df ['1.6.1.e<=1.6.1.d'],
                        df ['2.1.1<=2.1'],
                        df ['3.1<=2.1'],
                        df ['3.1.1<=3.1'],
                            df ['4.1.1.a+4.1.1.b+4.1.3>=2.1'],
                            df ['4.1.2<=4.1.1.a+4.1.1.b'],
                            df ['4.3.2.a<=4.3.1.a+4.3.1.b+4.2'],
                            df ['4.3.2.b<=4.3.2.a'],
                            df ['4.3.3<=4.3.1.a+4.3.1.b+4.2'],
                            df ['4.4.1<=4.1.1.a+4.1.1.b'],
                            df ['4.4.2<=4.4.1'],
                            df ['4.4.3<=4.1.1.a+4.1.1.b'],
                            df ['5.2<=5.1'],
                            df ['6.3<=2.1'],
                                df ['6.4<=2.1'],
                                df ['7.2.1<=7.1.1'],
                                df ['7.2.2<=7.1.2'],
                                df ['8.2.3<=2.1'],
                                df ['8.4<=2.1'],
                                df ['8.7<=8.3+8.4+8.5'],
                                df ['8.17.1<=8.1.1'],
                                df ['8.17.2<=8.2.1+8.2.2+8.2.3+8.2.4'],
                                df ['9.1.1<=4.1.1.a+4.1.1.b'],
                                df ['9.1.2<=4.1.1.a+4.1.1.b'],
                                    df ['9.1.9<=4.1.1.a+4.1.1.b'],
                                    df ['9.1.13<=4.1.1.a+4.1.1.b'],
                                    df ['9.2.4.a+9.2.4.b<=9.2.1+ 9.2.2'],
                                    df ['11.2.2<=11.2.1'],
                                    df ['12.1.2.a<=12.1.1.a'],
                                    df ['12.1.2.b<=12.1.1.b'],
                                    df ['12.1.3.a<=12.1.1.a'],
                                    df ['12.1.3.b<=12.1.1.b'],
                                    df ['14.2.1+14.2.2>=14.1.1+14.1.2+14.1.3+14.1.4+14.1.5+14.1.6+14.1.7+14.1.8+14.1.9'],
                                    df ['14.3.3<=14.3.1.a+14.3.1.b+14.3.2.a+14.3.2.b'],
                                    df ['14.4.1<=14.3.1.a+14.3.1.b+14.3.2.a+14.3.2.b'],
                                        df ['14.4.2<=14.3.1.a+14.3.1.b+14.3.2.a+14.3.2.b'],
                                        df ['14.4.3<=14.3.1.a+14.3.1.b+14.3.2.a+14.3.2.b'],
                                        df ['14.4.4<=14.3.1.a+14.3.1.b+14.3.2.a+14.3.2.b'],
                                        df ['14.4.5<=14.3.1.a+14.3.1.b+14.3.2.a+14.3.2.b'],
                                        df ['14.4.6<=14.3.1.a+14.3.1.b+14.3.2.a+14.3.2.b'],
                                        df ['14.4.7<=14.3.1.a+14.3.1.b+14.3.2.a+14.3.2.b'],
                                        df ['14.4.8<=14.3.1.a+14.3.1.b+14.3.2.a+14.3.2.b'],
                                        df ['14.6.1<=14.5'],
                                        df ['14.6.2<=14.5'],
                                        df ['14.6.3<=14.5'],
                                        df ['14.6.4<=14.5'],
                                        df ['14.6.5<=14.5'],
                                            df ['14.7<=14.5'],
                                            df ['14.14.2<=14.14.1'],
                                            df ['15.2.2<=15.2.1'],
                                            df ['15.3.2.b<=15.3.2.a'],
                                            df ['15.3.3.b<=15.3.3.a'],
                                            df ['15.3.3.c<=15.3.3.b'],
                                            df ['15.4.2<=15.4.1'],
                                            df ['9.6.1<=9.1.1+9.1.2+9.1.3+9.1.4+9.1.5+9.1.6+9.1.7+9.1.8+9.1.13+9.1.14+9.1.15+9.1.16+9.1.17+9.1.18+9.1.19+9.1.20+9.1.21+9.2.1+9.2.2+9.2.3+9.3.1+9.3.2+9.3.3+9.4.1+9.4.2+9.4.3+9.4.5+9.4.6+9.5.1+9.5.2+9.5.3+9.5.4'],
                                            df ['9.6.2<=9.1.1+9.1.2+9.1.3+9.1.4+9.1.5+9.1.6+9.1.7+9.1.8+9.1.13+9.1.14+9.1.15+9.1.16+9.1.17+9.1.18+9.1.19+9.1.20+9.1.21+9.2.1+9.2.2+9.2.3+9.3.1+9.3.2+9.3.3+9.4.1+9.4.2+9.4.3+9.4.5+9.4.6+9.5.1+9.5.2+9.5.3+9.5.4'],
                                            df ['9.6.3<=9.1.1+9.1.2+9.1.3+9.1.4+9.1.5+9.1.6+9.1.7+9.1.8+9.1.13+9.1.14+9.1.15+9.1.16+9.1.17+9.1.18+9.1.19+9.1.20+9.1.21+9.2.1+9.2.2+9.2.3+9.3.1+9.3.2+9.3.3+9.4.1+9.4.2+9.4.3+9.4.5+9.4.6+9.5.1+9.5.2+9.5.3+9.5.4'],
                                            df ['9.7.2<=9.7.1'],
                                            df ['9.7.3<=9.7.2'],
                                                df ['11.1.1.b<=11.1.1.a'],
                                                df ['11.1.1.c<=11.1.1.a'],
                                                df ['11.1.2.b<=11.1.2.a'],
                                                df ['11.1.2.c<=11.1.2.a'],
                                                df ['14.9.1<=14.3.1.a+14.3.1.b'],
                                                df ['14.9.2<=14.3.2.a+14.3.2.b'],
                                                df ['14.13<=14.12.1+14.12.2+14.12.3+14.12.4+14.12.5'],
                                                df ['14.8.2<=14.8.1'],
                                                df ['15.3.4.b<=15.3.4.a'],
                                                df ['15.3.4.d<=15.3.4.c']], axis=1)

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
    self.msg.setText("Community Health Centre validation successfully complete.")
    # Set the title of the window
    self.msg.setWindowTitle("Validation Successful Message")
    # Display the message box
    self.msg.show()

    return df

# To reference df
def load_CHC(self):
    return df
