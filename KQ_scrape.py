from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

def scrape_all():
   
   data = {
    "title":title,
    "paragraph": paragraph,
    "datatable": datatable
}




