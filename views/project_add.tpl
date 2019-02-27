<html>
    <head>
        <title>Projects</title>
    </head>
    <body>
        <h1>Add a project</h1>
        <form action="/project/add" method="post">
            <div>
                <label for="name">Project Name:</label>
                <input type="text" id="name" name="project_name">
            </div>
            <div class="button">
                <button type="submit">Add project</button>
            </div>
        </form>
    </body>
</html>