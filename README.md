#Nirvaris Menu


A simple Django app to for a menu to be used with Nirvaris Themes.

#Quick start

To install the Dictionary, use pip from git:

```
pip install git+https://github.com/nirvaris/nirvaris-menu
```

```
INSTALLED_APPS = (
        ...
        'menu',
        'n_profile',
        'themedefault'
)
```

You have to run migrate, as it uses the db to store the menu.

