<html>
    <head>
        <title>Tasks for {{project_name}}</title>
    </head>
    <body>
        <h1>Tasks for {{project_name}}</h1>
        <i>{{!message}}</i>

        <ul>
            % for task in tasks:
                <li>{{task}}</li>
            % end
        </ul>
        <a href="/project/{{project_id}}/tasks/add">Add a new task</a>
    </body>
</html>