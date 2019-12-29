from flask import Blueprint, flash, redirect, request, render_template, url_for

bp = Blueprint('index', __name__)


@bp.route('/')
def register():
    return render_template('index/index.html')
