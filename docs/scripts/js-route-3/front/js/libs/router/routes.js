export default [
    {re: /about/, action: 'about@PagesController'},
    {re: /contact/, action: 'contact@PagesController'},
    {re: /project-([0-9]+)-([0-9a-z-]+)/i, action: 'project@ProjectsController'},
]
