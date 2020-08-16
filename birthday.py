import pandas as pd 
import datetime
import smtplib
GMAIL_ID=''
GMAIL_PSWD=''
def sendEmail(to,sub,msg):
    print(f"Email to {to} sent with subject:{sub} and message {msg}")
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(GMAIL_ID,GMAIL_PSWD)
    s.sendmail(GMAIL_ID,to,f"Subject:{sub}\n{msg}")
    s.quit()
if __name__ == "__main__":
    # sendEmail(GMAIL_ID,"subject","testmessage")
    # exit()
    df=pd.read_excel("birthday wisher.xlsx")
    # print(df)
    today=datetime.datetime.now().strftime("%d-%m")
    yearNow=datetime.datetime.now().strftime("%Y")
    # print(today)
    writeInd=[]
    for index,item in df.iterrows():
        # print(index,item['Birthday'])
        bday=item['Birthday'].strftime("%d-%m")
        
        if today==bday and yearNow not in str(item['Year']):
            sendEmail(item['Email'],"Happy Birthday",item['Dialogue'])
            writeInd.append(index)
    # print(writeInd)
    for i in writeInd:
        yr=df.loc[i,'Year']
        print(yr)
        df.loc[i,'Year']=f"{str(yr)},{str(yearNow)}"
        # print(df.loc[i,'Year'])
    # print(df)
    df.to_excel('birthday wisher.xlsx',index=False)


