#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
import codecs
import re

def build_soup(url):
    '''Creates the soup'''
    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.text, 'html.parser')
    return soup

def build_title(soup, num):
    '''Produces a name from the soup'''
    title = soup.h2
    filename = str(num) + '_' + title.text.replace(' ', '_') + '.py'
    translation_table = dict.fromkeys(map(ord, '!@#$/;:?'), None)
    return filename.translate(translation_table)

def build_description(soup):
    '''Produces the description from the soup'''
    return soup.find('div', {'class': 'problem_content'}).text
    
def write_file(filename, description):
    '''Writes file to current directory'''
    line_break = '-'*100 + '\n'
    fo = codecs.open(filename, 'w', encoding='utf-8')
    fo.write('#!/usr/bin/python \n\n' +
             '""" \n\n' +
             line_break + filename + '\n' + line_break + '\n' +
             line_break + 'Description' + '\n' + line_break +
             description + '\n' +
             '""" \n\n')
    fo.close()
        
def euler_script(stop, start=1):
    '''Run the script'''
    url = 'https://projecteuler.net/problem='
    problem_range = range(start,stop+1)
    for num in problem_range:
        problem_url = url+str(num)
        soup = build_soup(problem_url)
        
        title = build_title(soup, num)
        description = build_description(soup)
        
        write_file(title, description)
        print('Created ' + title)
    print('Script ran successfully!')


if __name__ == "__main__":
    euler_script(10)
    
