package com.nikhil.myfirstapp;

/**
 * Created by Nikhil on 4/12/2015.
 */
public class DisplayMessageActivity {
    public static void main()
    {
        double inp=0;
        if((inp>=06001  && inp<=6389))
            System.out.println("Welcome to State of Connecticut. You can find the nearest Capital one bank ATM by clicking the following link: \n https://secure.capitalone360.com/myaccount/banking/atm_locate.vm");
        else if ((inp>=20001 && inp<=20039) && (inp>=20042 && inp<=20599))
            System.out.println("Welcome to District of Columbia.  You can find the nearest Capital one bank ATM by clicking the following link: \n https://secure.capitalone360.com/myaccount/banking/atm_locate.vm");
        else if(inp>=19701 && inp<= 19980)
            System.out.println("Welcome to State of Delaware.  You can find the nearest Capital one bank ATM by clicking the following link: \n https://secure.capitalone360.com/myaccount/banking/atm_locate.vm");
        else if((inp>=70001 && inp<=71232) && (inp>=71234 && inp<=71497))
            System.out.println("Welcome to State of Delaware.  You can find the nearest Capital one bank ATM by clicking the following link: \n https://secure.capitalone360.com/myaccount/banking/atm_locate.vm");
        else if(inp==20331 &&(inp>=20335 && inp<=20797) && (inp>=20812 && inp<=21930))
            System.out.println("Welcome to State of Maryland.  You can find the nearest Capital one bank ATM by clicking the following link: \n https://secure.capitalone360.com/myaccount/banking/atm_locate.vm");
        else if((inp>=07001  && inp<=8989))
            System.out.println("Welcome to State of New Jersey.  You can find the nearest Capital one bank ATM by clicking the following link: \n https://secure.capitalone360.com/myaccount/banking/atm_locate.vm");
        else if((inp>=10001  && inp<=14975))
            System.out.println("Welcome to State of New York.  You can find the nearest Capital one bank ATM by clicking the following link: \n https://secure.capitalone360.com/myaccount/banking/atm_locate.vm");
        else if((inp>=75001 && inp<=75501) && (inp>=75503 && inp<=79999))
            System.out.println("Welcome to State of Texas.  You can find the nearest Capital one bank ATM by clicking the following link: \n https://secure.capitalone360.com/myaccount/banking/atm_locate.vm");
        else if((inp>=20040 && inp<=20167) && (inp>=22001 && inp<=24658))
            System.out.println("Welcome to State of Virginia.  You can find the nearest Capital one bank ATM by clicking the following link: \n https://secure.capitalone360.com/myaccount/banking/atm_locate.vm");
        else if((inp>=99501  && inp<=99950))
            System.out.println("Welcome to State of Alaska.\n Congratulations, you have saved your time and fuel by not travelling 3098 miles, in order to get to your nearest capital one bank ATM. You can find the nearest Surcharge free ATM by clicking the following link: \n http://www.moneypass.com/atm-locator.aspx");






    }

}
