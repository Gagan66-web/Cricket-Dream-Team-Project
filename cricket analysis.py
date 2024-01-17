import random
import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


root = Tk()
root.title("DREAM TEAM")
root2 = Toplevel(root)
root2.title("DREAM TEAM") 
root2.withdraw()

bg_image = PhotoImage(file="C:\\Users\\Comp\\Downloads\\cricket.png")
bg_label = Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label2 = Label(root2, image=bg_image)
bg_label2.place(x=0, y=0, relwidth=1, relheight=1)


con=mysql.connector.connect(host="localhost",
                          user="root",
                          passwd="boot",
                          database="cricket")

nrr = 0

def addmore():
    eas = messagebox.askyesno("DREAM TEAM", "Add more players?")
    if eas:
        clr = messagebox.askyesno("DREAM TEAM", "Clear the prvious inputs?")
        if clr:
            cur=con.cursor()
            cur.execute("Delete from Dream_Team")
            con.commit()
            root2.withdraw()
            root.deiconify()
            insert1()
        else:
            root2.withdraw()
            root.deiconify()
            insert1()
    else:
        tr = messagebox.askyesno("DREAM TEAM", "Try Again from scratch?")
        if tr:
            cur=con.cursor()
            cur.execute("Delete from Dream_Team")
            con.commit()
            root2.withdraw()
            root.deiconify()
            insert1()
        else:
            messagebox.showinfo("DREAM TEAM", "Thank you for playing...\nFeel free to play again")
              
        
def newwin():
    def rating():
        table.destroy()
        lf1.destroy()
        ld.destroy()
        lr.grid_forget()
        br.grid_forget()
        root.withdraw()
        root2.deiconify()
        lr0 = Label(root2, text = "HERE IS YOUR TEAM'S RATING!", font=('Helvetica', 10), bg = "black", fg = 'cyan')
        lr0.grid(row = 0, columnspan = 3, padx = 5, pady = 5)
        lno = Label(root2, text = "Enter the number of overs: ", font=('Helvetica', 10), bg = "black", fg = 'cyan')
        lno.grid(row = 1, column = 0, padx = 5, pady = 5)
        eno = Entry(root2)
        eno.grid(row = 1, column = 1, padx = 5, pady = 5)
    
        def nrr1():
            cur=con.cursor()
            try:
                s="select sum(Score) from Dream_Team"
                cur.execute(s)
                result=cur.fetchone()
                for i in result:
                    global nrr
                    nrr =i/int(eno.get())
                    lnrr = Label(root2 ,text = "Net Run rate: "+str(round(nrr,2)), font=('Helvetica', 10), bg = "black", fg = 'cyan')
                    lnrr.grid(row = 2, columnspan = 3, padx = 5, pady = 5)
                    skr()
            except ZeroDivisionError:
                print("Overs faced cannot be zero!!!!")
    
        def disp():
            if nrr>=7 and nrr < 9:
                lr1 = Label(root2, text = "YOUR TEAM HAS A GOOD PERFORMANCE", font=('Helvetica', 10), bg = "black", fg = 'cyan')
                lr1.grid(row = 5, columnspan = 3, padx = 5, pady = 5)
                lr2 = Label(root2, text = "Team Rating: "+str(random.randrange(80,95)), font=('Helvetica', 10), bg = "black", fg = 'cyan')
                lr2.grid(row = 6, columnspan = 3, padx = 5, pady = 5)
            elif nrr>=9:
                lr1 = Label(root2, text = "YOUR TEAM HAS A REMARKABLE PERFORMANCE!!!", font=('Helvetica', 10), bg = "black", fg = 'cyan')
                lr1.grid(row = 5, columnspan = 3, padx = 5, pady = 5)
                lr2 = Label(root2, text = "Team rating:"+str(random.randrange(95,100)), font=('Helvetica', 10), bg = "black", fg = 'cyan')
                lr2.grid(row = 6, columnspan = 3, padx = 5, pady = 5)
            elif nrr<7:
                lr1 = Label(root2, text = "YOUR TEAM HAS POTENTIAL... CAN PERFORM BETTER", font=('Helvetica', 10), bg = "black", fg = 'cyan')
                lr1.grid(row = 5, columnspan = 3, padx = 5, pady = 5)
                lr2 = Label(root2, text = "Team Rating: "+str(random.randrange(70,80)), font=('Helvetica', 10), bg = "black", fg = 'cyan')
                lr2.grid(row = 6, columnspan = 3, padx = 5, pady = 5)
            addmore()

        def eco():
            cur=con.cursor()
            cur.execute("select avg(economy) from Dream_Team")
            result=cur.fetchone()
            for i in result:
                leco = Label(root2, text = "Average Economy of The Team: "+ str(round(i,2)), font=('Helvetica', 10), bg = "black", fg = 'cyan')
                leco.grid(row = 4, columnspan = 3, padx = 5, pady = 5)
            disp()
                
        def skr():
            cur=con.cursor()
            cur.execute("select avg(STRIKE_RATE) from Dream_Team")
            result=cur.fetchone()
            for i in result:
                lskr = Label(root2, text ="Average Strike rate of The Team: "+ str(round(i,2)), font=('Helvetica', 10), bg = "black", fg = 'cyan')
                lskr.grid(row = 3, columnspan = 3, padx = 5, pady = 5)
                eco()
                        
        bno = Button(root2, text = "Submit", command = nrr1)
        bno.grid(row = 1, column = 2, padx = 5, pady = 5)
    lf1 = Label(root, text = "DREAM TEAM CREATED!!", font=('Helvetica', 10), bg = "black", fg = 'cyan')
    lf1.grid(row = 0)
    ld = Label(root, text = "HERE IS YOUR TEAM -", font=('Helvetica', 10), bg = "black", fg = 'cyan')
    ld.grid(row = 1, padx = 5, pady = 5)
    cur=con.cursor()
    query=("Select * from Dream_Team")
    cur.execute(query)
    result=cur.fetchall()
    table = ttk.Treeview(root, columns = ('Name','Runs Scored','Balls Played','Runs Conceded','Overs Bowled','Strike Rate','Economy'), show='headings')
    table.heading('Name', text = 'Name')
    table.heading('Runs Scored', text = 'Runs Scored', anchor = CENTER)
    table.heading('Balls Played', text = 'Balls Played', anchor = CENTER)
    table.heading('Runs Conceded', text = 'Runs Conceded', anchor = CENTER)
    table.heading('Overs Bowled', text = 'Overs Bowled', anchor = CENTER)
    table.heading('Strike Rate', text = 'Strike Rate', anchor = CENTER)
    table.heading('Economy', text = 'Economy', anchor = CENTER)
    table.column('Name', width = 100)
    table.column('Runs Scored', width = 100)
    table.column('Balls Played', width = 100)
    table.column('Runs Conceded', width = 100)
    table.column('Overs Bowled', width = 100)
    table.column('Strike Rate', width = 100)
    table.column('Economy', width = 100)
    for item in result:
        table.insert("", "end", values=item)
    table.grid(row = 2)
    lr = Label(root, text = "Check the rating of your team:", font=('Helvetica', 10), bg = "black", fg = 'cyan')
    lr.grid(row = 3, columnspan = 3,padx = 5, pady = 5)
    br = Button(root, text = "Rating", command = rating, font=('Helvetica', 10), bg = "black", fg = 'cyan')
    br.grid(row = 4, columnspan = 3)
                
def insert1():
    lf = Label(root,text = "CREATE YOUR DREAM TEAM!", font=('Helvetica', 10), bg = "black", fg = 'cyan')
    lf.grid(row = 0, columnspan = 3, padx = 5, pady = 5)
    cur=con.cursor()
    c = [0]
    def insert2():
        bnp.config(state=DISABLED)
        if c[0] < int(enp.get()):
            c[0] += 1
            lpn = Label(root, text = "PLAYER " + str(c[0]) + ":", font=('Helvetica', 10), bg = "black", fg = 'cyan')
            lpn.grid(row = 2, column = 0, padx = 5, pady = 5)
            ln = Label(root, text = "Enter Name", font=('Helvetica', 10), bg = "black", fg = 'cyan')
            ln.grid(row = 3, column = 0, padx = 5, pady = 5)
            en = Entry(root, width = 30)
            en.grid(row = 3, column = 1, padx = 5, pady = 5)
            lp = Label(root, text = "Player type", font=('Helvetica', 10), bg = "black", fg = 'cyan')
            lp.grid(row = 4, column = 0, padx = 5, pady = 5)
            var = StringVar()
            pt = OptionMenu(root, var, "Batsman", "All Rounder", "Bowler")
            pt.grid(row = 4, column = 1, padx = 5, pady = 5)
            var.set("Select")
            def insert3():
                bi.config(state=DISABLED)
                if var.get()=="Batsman":
                    ls = Label(root, text = "Enter the score of player", font=('Helvetica', 10), bg = "black", fg = 'cyan')
                    ls.grid(row = 5, column = 0, padx = 5, pady = 5)
                    es = Entry(root)
                    es.grid(row = 5, column = 1, padx = 5, pady = 5)
                    lbp = Label(root, text = "Enter number of balls played", font=('Helvetica', 10), bg = "black", fg = 'cyan')
                    lbp.grid(row = 6, column = 0, padx = 5, pady = 5)
                    ebp = Entry(root)
                    ebp.grid(row = 6, column = 1, padx = 5, pady = 5)
                    def bat1():
                        bba.config(state=DISABLED)
                        r=0
                        s=0
                        strike=round((int(es.get())//int(ebp.get()))*100,2)
                        economy=0
                        query1="Insert into Dream_Team values('{}','{}','{}','{}','{}','{}','{}')".format(en.get(),es.get(),ebp.get(),r,s,strike,economy)        
                        cur.execute(query1)
                        con.commit()
                        m = "Player " + str(c[0]) + " of " + enp.get() + " players DONE!"
                        messagebox.showinfo("DREAM TEAM", m)
                        def destroy1():
                            ls.destroy()
                            es.destroy()
                            lbp.destroy()
                            ebp.destroy()
                            ba.destroy()
                            bba.destroy()
                            pt.destroy()
                            en.destroy()
                            ln.destroy()
                            lpn.destroy()
                            lp.destroy()
                            bi.destroy()
                            insert2()
                        if c[0] == int(enp.get()):
                            ba = Button(root, text = "Finish", command = destroy1, font=('Helvetica', 10), bg = "black", fg = 'cyan')
                            ba.grid(row = 7, columnspan = 3)
                        else:    
                            ba = Button(root, text = "Next player..", command = destroy1, font=('Helvetica', 10), bg = "black", fg = 'cyan')
                            ba.grid(row = 7, columnspan = 3)    
                    bba = Button(root, text = "Submit", command = bat1, font=('Helvetica', 10), bg = "black", fg = 'cyan')
                    bba.grid(row = 6, column = 2, padx = 5, pady = 5)
                    
                elif var.get()=="Bowler":
                    lrc = Label(root, text = "Runs conceded", font=('Helvetica', 10), bg = "black", fg = 'cyan')
                    lrc.grid(row = 5, column = 0, padx = 5, pady = 5)
                    erc = Entry(root)
                    erc.grid(row = 5, column = 1, padx = 5, pady = 5)
                    lob = Label(root, text = "Number of overs done", font=('Helvetica', 10), bg = "black", fg = 'cyan')
                    lob.grid(row = 6, column = 0, padx = 5, pady = 5)
                    eob = Entry(root)
                    eob.grid(row = 6, column = 1, padx = 5, pady = 5)
                    def bowl1():
                        bba.config(state=DISABLED)
                        p=0
                        q=0
                        economy=round(int(erc.get())/int(eob.get()),2)
                        strike=0
                        query2="Insert into Dream_Team values('{}','{}','{}','{}','{}','{}','{}')".format(en.get(),p,q,erc.get(),eob.get(),strike,economy)  
                        cur.execute(query2)
                        con.commit()
                        m = "Player " + str(c[0]) + " of " + enp.get() + " players DONE!"
                        messagebox.showinfo("DREAM TEAM", m)
                        def destroy2():
                            lrc.destroy()
                            erc.destroy()
                            lob.destroy()
                            eob.destroy()
                            ba.destroy()
                            bba.destroy()
                            lpn.destroy()
                            pt.destroy()
                            en.destroy()
                            ln.destroy()
                            lp.destroy()
                            bi.destroy()
                            insert2()
                        if c[0] == int(enp.get()):
                            ba = Button(root, text = "Finish", command = destroy2, font=('Helvetica', 10), bg = "black", fg = 'cyan')
                            ba.grid(row = 7, columnspan = 3)
                        else:    
                            ba = Button(root, text = "Next player..", command = destroy2, font=('Helvetica', 10), bg = "black", fg = 'cyan')
                            ba.grid(row = 7, columnspan = 3)    
                    bba = Button(root, text = "Submit", command = bowl1)
                    bba.grid(row = 6, column = 2, padx = 5, pady = 5)
           
                elif var.get()=="All Rounder":
                    ls = Label(root, text = "Enter the score of player", font=('Helvetica', 10), bg = "black", fg = 'cyan')
                    ls.grid(row = 5, column = 0, padx = 5, pady = 5)
                    es = Entry(root)
                    es.grid(row = 5, column = 1, padx = 5, pady = 5)
                    lbp = Label(root, text = "Enter number of balls played", font=('Helvetica', 10), bg = "black", fg = 'cyan')
                    lbp.grid(row = 6, column = 0, padx = 5, pady = 5)
                    ebp = Entry(root)
                    ebp.grid(row = 6, column = 1, padx = 5, pady = 5)
                    lrc = Label(root, text = "Runs conceded", font=('Helvetica', 10), bg = "black", fg = 'cyan')
                    lrc.grid(row = 7, column = 0, padx = 5, pady = 5)
                    erc = Entry(root)
                    erc.grid(row = 7, column = 1, padx = 5, pady = 5)
                    lob = Label(root, text = "Number of overs done", font=('Helvetica', 10), bg = "black", fg = 'cyan')
                    lob.grid(row = 8, column = 0, padx = 5, pady = 5)
                    eob = Entry(root)
                    eob.grid(row = 8, column = 1, padx = 5, pady = 5)
                    def all1():
                        bba.config(state=DISABLED)
                        economy=(int(erc.get()))/int(eob.get())
                        strike=(int(es.get())//int(ebp.get()))*100
                        query2="Insert into Dream_Team values('{}','{}','{}','{}','{}','{}','{}')".format(en.get(),es.get(),ebp.get(),erc.get(),eob.get(),strike,economy)  
                        cur.execute(query2)
                        con.commit()
                        m = "Player " + str(c[0]) + " of " + enp.get() + " players DONE!"
                        messagebox.showinfo("DREAM TEAM", m)
                        def destroy3():
                            ls.destroy()
                            es.destroy()
                            lbp.destroy()
                            ebp.destroy()
                            lrc.destroy()
                            erc.destroy()
                            lpn.destroy()
                            lob.destroy()
                            eob.destroy()
                            ba.destroy()
                            bba.destroy()
                            pt.destroy()
                            en.destroy()
                            ln.destroy()
                            lp.destroy()
                            bi.destroy()
                            insert2()
                        if c[0] == int(enp.get()):
                            ba = Button(root, text = "Finish", command = destroy3, font=('Helvetica', 10), bg = "black", fg = 'cyan')
                            ba.grid(row = 9, columnspan = 3)
                        else:    
                            ba = Button(root, text = "Next player..", command = destroy3, font=('Helvetica', 10), bg = "black", fg = 'cyan')
                            ba.grid(row = 9, columnspan = 3)   
                    bba = Button(root, text = "Submit", command = all1)
                    bba.grid(row = 8, column = 2, padx = 5, pady = 5)
                    
            bi = Button(root, text = "Submit", command = insert3, font=('Helvetica', 10), bg = "black", fg = 'cyan')
            bi.grid(row = 4, column = 2, padx = 5, pady = 5)
        else:
            lf.destroy()
            lnp.destroy()
            bnp.destroy()
            enp.destroy()
            newwin()
                    
    lnp = Label(root, text = "Enter the number of cricket players in your Team: ", font=('Helvetica', 10), bg = "black", fg = 'cyan')
    lnp.grid(row = 1, column = 0, padx = 5, pady = 5)
    enp = Entry(root)
    enp.grid(row = 1, column = 1, padx = 5, pady = 5)
    def check1():
        e = enp.get()
        if e.strip() == '':
            messagebox.showwarning("DREAM TEAM", "Number of players cannot be zero \n The entry field cant be empty!!") 
        elif int(e) == 0:
            messagebox.showwarning("DREAM TEAM", "Number of players cannot be zero!!")
        elif int(e) > 0:
            insert2()
    bnp = Button(root, text = "Submit", command = check1, font=('Helvetica', 10), bg = "black", fg = 'cyan')
    bnp.grid(row = 1, column = 2, padx = 5, pady = 5)
    

insert1()

root.mainloop()
