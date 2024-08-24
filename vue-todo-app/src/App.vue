<template>
  <div id="app">
    <h1>Todo App</h1>
    <input 
      v-model="newTodo" 
      @keyup.enter="addTodo" 
      placeholder="Add a new todo"
    >
    <ul>
      <li v-for="(todo, index) in todos" :key="index">
        <input 
          type="checkbox" 
          v-model="todo.completed"
        >
        <span :class="{ completed: todo.completed }">{{ todo.text }}</span>
        <button @click="removeTodo(index)">Delete</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      newTodo: '',
      todos: [
        { text: 'Learn Vue', completed: false },
        { text: 'Build a todo app', completed: false },
        { text: 'Master Vue', completed: false }
      ]
    }
  },
  methods: {
    addTodo() {
      if (this.newTodo.trim().length === 0) {
        return
      }
      this.todos.push({ text: this.newTodo, completed: false })
      this.newTodo = ''
    },
    removeTodo(index) {
      this.todos.splice(index, 1)
    }
  }
}
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
}

input[type="text"] {
  width: 100%;
  padding: 5px;
  margin-bottom: 10px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: flex;
  align-items: center;
  margin-bottom: 5px;
}

.completed {
  text-decoration: line-through;
  color: #888;
}

button {
  margin-left: 10px;
}
</style>