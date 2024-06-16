import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import ProjectList from './components/ProjectList';
import ProjectDetail from './components/ProjectDetail';
import TaskList from './components/TaskList';
import TaskDetail from './components/TaskDetail';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/projects/:id" component={ProjectDetail} />
        <Route path="/projects" component={ProjectList} />
        <Route path="/tasks/:id" component={TaskDetail} />
        <Route path="/tasks" component={TaskList} />
      </Switch>
    </Router>
  );
}

export default App;
