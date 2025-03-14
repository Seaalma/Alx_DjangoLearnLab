<!-- Example: book_list.html or form_example.html -->
<form method="POST">
    {% csrf_token %}
    <!-- Other form fields go here -->
    <input type="submit" value="Submit">
</form>
