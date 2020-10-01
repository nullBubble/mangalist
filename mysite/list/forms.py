from django import forms

class chapterForm(forms.Form):
    chapter = forms.IntegerField(label='', required=False)

#<label>Chapter</label>
#<input id="chapter" type="number" style="width:70px" name="chapter" value="{{entry.current_chapter}}">

