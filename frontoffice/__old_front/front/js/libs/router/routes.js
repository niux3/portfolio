export default [
    {re: /home/, action: 'home@PagesController'},
    {re: /about/, action: 'about@PagesController'},
    {re: /contact/, action: 'contact@PagesController'},
    {re: /project-([0-9]+)-([0-9a-z-]+)/i, action: 'project@ProjectsController'},
]
