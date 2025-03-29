from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from backend.portfolio.forms import CommonForm, PortfolioForm, ActivityForm
from backend import db
from backend.portfolio.models import Function, Technology, Portfolio, PortfolioTechnology, Activity


bp = Blueprint('portfolio', __name__)

