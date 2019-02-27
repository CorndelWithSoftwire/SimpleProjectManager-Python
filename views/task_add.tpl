<html>
    <head>
        <title>Tasks</title>
    </head>
    <body>
        <h1>Add a task for {{project_name}}</h1>
        <form action="/project/{{project_id}}/tasks/add" method="post">
            <div>
                <label for="name">Task Name:</label>
                <input type="text" id="name" name="task_name">
            </div>
            <div class="button">
                <button type="submit">Add task</button>
            </div>
        </form>
    </body>
</html>