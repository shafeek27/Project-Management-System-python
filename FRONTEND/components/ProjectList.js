import React, { useEffect, useState } from 'react';
import { getProjects } from '../api';

function ProjectList() {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    getProjects().then(response => {
      setProjects(response.data);
    });
  }, []);

  return (
    <div>
      <h1>Projects</h1>
      <ul>
        {projects.map(project => (
          <li key={project.project_id}>{project.project_name}</li>
        ))}
      </ul>
    </div>
  );
}

export default ProjectList;
