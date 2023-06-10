


"Using SQL, create a database for a simple todo list program that has the following columns: task_id (primary key), task_name, description, and is_completed."

Here is an example SQL script for creating a database for a simple todo list program:

```
CREATE DATABASE todo_list;

USE todo_list;

CREATE TABLE tasks (
  task_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  task_name VARCHAR(255) NOT NULL,
  description TEXT,
  is_completed BOOLEAN NOT NULL DEFAULT FALSE
);
```

This script creates a new database called `todo_list` and a table called `tasks`. The `tasks` table has four columns: `task_id` (the primary key), `task_name`, `description`, and `is_completed`. The `is_completed` column is set to default to `false` for each new task added to the list.
