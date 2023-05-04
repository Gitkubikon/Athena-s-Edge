import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, GLib, Gdk, Gio
import json
import os

CONTENT_FOLDER = "content"
METADATA_FILE = "metadata.json"

metadata = {}

try:
    with open(os.path.join(CONTENT_FOLDER, METADATA_FILE), "r") as f:
        metadata = json.load(f)
except FileNotFoundError:
    print(f"Metadata file {METADATA_FILE} not found")
except json.JSONDecodeError as e:
    print(f"Error loading metadata file: {e}")

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Welcome to Athena's Admin Panel")

        # Set the window size and position
        self.set_default_size(600, 400)
        self.set_position(Gtk.WindowPosition.CENTER)

        # Create a vertical box layout
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)

        # Create a stack and add the vbox to it
        stack = Gtk.Stack()
        stack.set_transition_duration(1000) # Set the duration of the transition animation
        stack.add_titled(vbox, "main", "Main")

        self.add(stack)

        # Load the logo image
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("logo.svg", 200, 200, True)
        image = Gtk.Image.new_from_pixbuf(pixbuf)
        vbox.pack_start(image, True, True, 0)

        # Add the welcome text
        welcome_label = Gtk.Label()
        welcome_label.set_text("Athena's Admin Panel")
        welcome_label.set_margin_top(20)
        welcome_label.set_margin_bottom(20)
        vbox.pack_start(welcome_label, False, False, 0)

        # Create a CSS provider and load the CSS file
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path("adminstyle.css")

        # Add the CSS provider to the Gtk Style Context
        context = Gtk.StyleContext()
        screen = Gdk.Screen.get_default()
        context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        # Create the home page
        home_page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=50)
        home_page.set_margin_top(20)
        home_page.set_margin_bottom(20)
        home_page.set_margin_start(50)
        home_page.set_margin_end(50)
        home_page.get_style_context().add_class("home-page")

        # Create the buttons
        dashboard_button = Gtk.Button.new_with_label("generate")
        generate_button = Gtk.Button.new_with_label("Generate")
        categorize_button = Gtk.Button.new_with_label("Categorize")
        scrape_button = Gtk.Button.new_with_label("Scrape")
        manage_button = Gtk.Button.new_with_label("Manage")

####################################################################################
####################################################################################
##########################################
##                                      ##
##      # Create the dashb. page        ##
##                                      ##
##########################################

        dashboard_page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=50)
        dashboard_page.set_margin_top(20)
        dashboard_page.set_margin_bottom(20)
        dashboard_page.set_margin_start(50)
        dashboard_page.set_margin_end(50)
        dashboard_page.get_style_context().add_class("dashboard-page")

        # Add widgets to the dashboard page
        dashboard_label = Gtk.Label()
        dashboard_label.set_text("This is the Dashboard page.")
        dashboard_page.pack_start(dashboard_label, True, True, 0)

        # Add the dashboard page to the stack
        stack.add_titled(dashboard_page, "dashboard", "Dashboard")

        # Connect the dashboard button to a callback function
        def on_dashboard_button_clicked(widget):
            stack.set_visible_child_name("dashboard")

        dashboard_button.connect("clicked", on_dashboard_button_clicked)

##########################################
##                                      ##
##      # Create the manage page        ##
##                                      ##
##########################################


        manage_page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=50)
        manage_page.set_margin_top(20)
        manage_page.set_margin_bottom(20)
        manage_page.set_margin_start(50)
        manage_page.set_margin_end(50)
        manage_page.get_style_context().add_class("manage-page")

        # Add widgets to the manage page
        manage_label = Gtk.Label()
        manage_label.set_text("This is the manage page.")
        manage_page.pack_start(manage_label, False, False, 0)


        # Add the manage page to the stack
        stack.add_titled(manage_page, "manage", "manage")

               # Add a box for each article
        for category, articles in metadata.items():
            for article_id, article_metadata in articles.items():
                article_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
                article_box.set_border_width(10)

                # Add a label for the article title
                title_label = Gtk.Label()
                # title_label.set_markup(f"<b>{article_metadata['category']}</b>")
                title_label.set_halign(Gtk.Align.START)
                article_box.pack_start(title_label, False, False, 0)

                # Add a label for the article description
                description_label = Gtk.Label()
                description_label.set_text(article_metadata['description'])
                description_label.set_halign(Gtk.Align.START)
                article_box.pack_start(description_label, False, False, 0)

                # Add the article box to the manage page
                manage_page.pack_start(article_box, False, False, 0)
                print(article_box)

        # Add the manage page to the stack
        stack.add_titled(manage_page, "manage", "manage")

        # Connect the manage button to a callback function
        def on_manage_button_clicked(widget):
            stack.set_visible_child_name("manage")

        manage_button.connect("clicked", on_manage_button_clicked)



##########################################
##                                      ##
##      # Create the scrape page        ##
##                                      ##
##########################################

        scrape_page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=50)
        scrape_page.set_margin_top(20)
        scrape_page.set_margin_bottom(20)
        scrape_page.set_margin_start(50)
        scrape_page.set_margin_end(50)
        scrape_page.get_style_context().add_class("scrape-page")

        # Add widgets to the scrape page
        scrape_label = Gtk.Label()
        scrape_label.set_text("This is the scrape page.")
        scrape_page.pack_start(scrape_label, True, True, 0)

        # Add the scrape page to the stack
        stack.add_titled(scrape_page, "scrape", "scrape")

        # Connect the scrape button to a callback function
        def on_scrape_button_clicked(widget):
            stack.set_visible_child_name("scrape")

        scrape_button.connect("clicked", on_scrape_button_clicked)


##########################################
##                                      ##
##      # Create the categ. page        ##
##                                      ##
##########################################

        categorize_page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=50)
        categorize_page.set_margin_top(20)
        categorize_page.set_margin_bottom(20)
        categorize_page.set_margin_start(50)
        categorize_page.set_margin_end(50)
        categorize_page.get_style_context().add_class("categorize-page")

        # Add widgets to the categorize page
        categorize_label = Gtk.Label()
        categorize_label.set_text("This is the categorize page.")
        categorize_page.pack_start(categorize_label, True, True, 0)

        # Add the categorize page to the stack
        stack.add_titled(categorize_page, "categorize", "categorize")

        # Connect the categorize button to a callback function
        def on_categorize_button_clicked(widget):
            stack.set_visible_child_name("categorize")

        categorize_button.connect("clicked", on_categorize_button_clicked)


##########################################
##                                      ##
##      # Create the gener. page        ##
##                                      ##
##########################################

        generate_page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=50)
        generate_page.set_margin_top(20)
        generate_page.set_margin_bottom(20)
        generate_page.set_margin_start(50)
        generate_page.set_margin_end(50)
        generate_page.get_style_context().add_class("generate-page")

        # Add widgets to the generate page
        generate_label = Gtk.Label()
        generate_label.set_text("This is the generate page.")
        generate_page.pack_start(generate_label, True, True, 0)

        # Add the generate page to the stack
        stack.add_titled(generate_page, "generate", "generate")

        # Connect the generate button to a callback function
        def on_generate_button_clicked(widget):
            stack.set_visible_child_name("generate")

        generate_button.connect("clicked", on_generate_button_clicked)

####################################################################################
####                                                                            ####
####################################################################################

        # Add the buttons to the home page
        home_page.pack_start(generate_button, True, True, 0)
        home_page.pack_start(generate_button, True, True, 0)
        home_page.pack_start(categorize_button, True, True, 0)
        home_page.pack_start(scrape_button, True, True, 0)
        home_page.pack_start(manage_button, True, True, 0)

        # Add the home page to the stack
        stack.add_titled(home_page, "home", "Home")


        # Set the initial page to the welcome page
        self.current_page = "home"

        # Create the animation for navigating to the home page
        transition = Gtk.StackTransitionType.SLIDE_LEFT
        stack.set_transition_type(transition)

        # Start the animation after 3 seconds
        GLib.timeout_add_seconds(2, self.animate)

    def animate(self):
        # Navigate to the home page with an animation
        self.get_child().set_visible_child_name(self.current_page)
        self.current_page = "main" if self.current_page == "home" else "home"

        # Stop the animation timer
        return False

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

