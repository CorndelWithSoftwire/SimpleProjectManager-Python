<html>
    <head>
        <title>Projects</title>
    </head>
    <body>
        <h1>Projects</h1>
        <ul>
            % for project in projects:
                <li>{{project}}</li>
            % end
        </ul>
    </body>
</html>