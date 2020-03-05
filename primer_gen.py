# -*- coding: utf-8 -*-
from random import uniform,seed,choice,randint
from time import time
from fpdf import FPDF, HTMLMixin
 
class HTML2PDF(FPDF, HTMLMixin):
    pass
 
def simple_table_html(out_name, prime_prob, body):
    pdf = HTML2PDF()
 
    table = """<table border="0" align="center" width="90%">
    <thead><tr><th width="33%">Primery: (prime prob: {})</th><th width="33%"></th><th width="34%"></th></tr></thead>
    <tbody>
    {}
    </tbody>
    </table>"""
 
    pdf.add_page()
    pdf.write_html(table.format(prime_prob,body))
    pdf.output('{}.pdf'.format(out_name))

def erato(n):
    pr = [True]*(n+1)
    pr[0] = False; pr[1] = False
    for i in range(2, n+1):
        if pr[i]:
            for j in range(i*i, n+1, i):
                pr[j] = True
    primes = []
    for i in range(n+1):
        if pr[i]:
            primes.append(i)
    return primes


def main():
    body = ""; body_answ = ""; """<tr><td>cell 1</td><td>cell 2</td></tr>
    <tr><td>cell 2</td><td>cell 3</td></tr>"""
    seed(time()) # set seed
    maxn = int(input("Please input maximum number: "))
    primes = erato(maxn)
    symbols = ['-','+']
    symb_mult = ['/','*']
    prime_prob = float(input("Please input prime equation probability: "))
    mult_prob = float(input("Please input multiplication(or division) probability: "))
    n = int(input("Enter equation number: "))
    for row in range(n//3+(1 if n%3 != 0 else 0)):
        srow = "<tr>"
        _srow = "<tr>"
        for col in range(3 if row < n//3 else n%3):
            srow += "<td>"
            _srow += "<td>"
            if uniform(0,1) > mult_prob:
                symb = choice(symbols)
                if uniform(0,1) <= prime_prob:
                    # prime
                    a=choice(primes[:-1])
                    if symb == '-':
                        print(a)
                        print(primes.index(a))
                        b=choice(primes[:primes.index(a)])
                    else:
                        b=choice(primes)
                else:
                    #non prime
                    a=randint(1,maxn)
                    if symb == '-':
                        b=randint(1,a)
                    else:
                        b=randint(1,maxn)
            else:
                # multiplication
                symb = choice(symb_mult)
                a = randint(2,10)
                if symb == '/':
                    b=1
                    for j in range(2,min(a+1,10+1)):
                        if a%j==0:
                            b=j
                            break
                else:
                    b=randint(2,10)
            res = eval(str(a)+symb+str(b))
            srow += "{} {} {} = ".format(a,symb,b)
            _srow += "{} {} {} = {}".format(a,symb,b,res)
            srow += "</td>"
            _srow += "</td>"
        srow+="</tr>"
        _srow+="</tr>"
        body+=srow+'\n'
        body_answ+=_srow+'\n'
    body += "<tr><td><b>Time:</b></td><td><b>Time:</b></td><td><b>Time:</b></td></tr>"
    simple_table_html('primery',prime_prob,body)
    simple_table_html('primery_answers',prime_prob,body_answ)
    return 0


if __name__ == "__main__":
    # simple_table_html()
    exit(main())