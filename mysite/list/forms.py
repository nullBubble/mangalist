from django import forms

class chapterForm(forms.Form):
    chapter = forms.Integerfield(label='Chapter', default=0)

#<label>Chapter</label>
#<input id="chapter" type="number" style="width:70px" name="chapter" value="{{entry.current_chapter}}">

