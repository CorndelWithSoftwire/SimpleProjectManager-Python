<html>
    <head>
        <title>Projects</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <h1>Projects</h1>
        <i>{{!message}}</i>

        <ul>
            % for project in projects:
                <li><a href='{{project['link']}}'>{{project['name']}}</a></li>
            % end
        </ul>
        <a href="/project/add">Add a new project</a>
    </body>
</html>