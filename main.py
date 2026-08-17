import datetime
import random
import flet as ft


# def main(page: ft.Page):
#   page.title = "For My Special Person ❤️"
#   page.vertical_alignment = ft.MainAxisAlignment.CENTER
#   page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#   page.bgcolor = "#ffe6e6"

#   start_date = datetime.date(2025,3,28)
#   today = datetime.date.today()
#   days_together = (today - start_date).days

#   # Expanded list of sweet, funny, and joyful responses
#   romantic_responses = [
#       "You just made me the happiest person alive! 🥰",
#       "My heart just did a flip! 💓",
#       "I knew you'd say yes! You're stuck with me now. 🤪",
#       "Best decision you've ever made! 🏆",
#       "To infinity and beyond together! 🚀✨",
#       "Every single day with you is a blessing. 🌸",
#       "You are my absolute favorite person. 🥇",
#       "Error 404: Heart completely overloaded with love! 💻❤️",
#       "Yay! Let's celebrate with snacks later. 🍕",
#       "You just locked in your forever best friend. 🔒💖",
#       "My smile is officially permanent now! 😁",
#       "Can we freeze this moment forever? ❄️✨",
#       "You hold the key to my heart, always. 🔑",
#       "Life is just better when we are a team. 🧑‍🤝‍🧑",
#       "I love you more than words can ever describe! 📚💞",
#       "Cue the romantic movie music! 🎬🎻",
#       "You make my world infinitely brighter. ☀️",
#       "Fairytales do exist, and you're mine. 🏰",
#       "I'm totally doing a happy dance right now! 💃🕺",
#       "You are the best thing that ever happened to me. 🌟",
#   ]

#   title_text = ft.Text(
#       "Will you be my forever?",
#       size=28,
#       weight=ft.FontWeight.BOLD,
#       color="#d63384",
#       text_align=ft.TextAlign.CENTER,
#   )

#   counter_text = ft.Text(
#       f"We have been smiling together for {days_together} days! 💕",
#       size=16,
#       color="#6c757d",
#       text_align=ft.TextAlign.CENTER,
#   )

#   def say_yes(e):
#     title_text.value = "Yaaay! 🥰"
#     # FIXED: Pulls a completely random phrase from the list on every click
#     counter_text.value = random.choice(romantic_responses)
#     no_button.visible = False
#     yes_button.scale = 1.2
#     page.update()

#   def move_no(e):
#     current_top = no_button.top if no_button.top is not None else 0
#     current_left = no_button.left if no_button.left is not None else 120

#     no_button.top = (current_top + 40) % 100
#     no_button.left = (current_left + 60) % 240
#     page.update()

#   yes_button = ft.Button(
#       content=ft.Text("Yes! ❤️", color=ft.Colors.WHITE, size=16),
#       on_click=say_yes,
#       style=ft.ButtonStyle(bgcolor="#e83e8c"),
#       top=0,
#       left=0,
#   )

#   no_button = ft.Button(
#       content=ft.Text("No", color=ft.Colors.WHITE, size=16),
#       on_hover=move_no,
#       style=ft.ButtonStyle(bgcolor="#6c757d"),
#       top=0,
#       left=120,
#   )

#   button_area = ft.Stack(
#       controls=[yes_button, no_button],
#       width=240,
#       height=150,
#   )

#   card_content = ft.Container(
#       content=ft.Column(
#           [
#               ft.Icon(ft.Icons.FAVORITE, color="#e83e8c", size=50),
#               title_text,
#               counter_text,
#               ft.Divider(height=20, color="transparent"),
#               button_area,
#           ],
#           horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#           alignment=ft.MainAxisAlignment.CENTER,
#       ),
#       padding=40,
#       bgcolor=ft.Colors.WHITE,
#       border_radius=20,
#       width=400,
#       shadow=ft.BoxShadow(
#           blur_radius=15,
#           spread_radius=5,
#           color="#f5c6cb",
#       ),
#   )

#   page.add(card_content)


# ft.run(main)

#pip install flet-audio

#"assets/muah-2.mp3"


import datetime
import random
import asyncio
import flet as ft
import flet_audio as fta

def main(page: ft.Page):
    page.title = "For My Special Person ❤️"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#ffe6e6"

    # Initialize and register the audio service
    audio = fta.Audio(src="muah-2.mp3")
    page.services.append(audio)

    start_date = datetime.date(2025, 3, 28)
    today = datetime.date.today()
    days_together = (today - start_date).days

    romantic_responses = [
        "You just made me the happiest person alive! 🥰",
        "My heart just did a flip! 💓",
        "I knew you'd say yes! You're stuck with me now. 🤪",
        "Best decision you've ever made! 🏆",
        "To infinity and beyond together! 🚀✨",
        "Every single day with you is a blessing. 🌸",
        "You are my absolute favorite person. 🥇",
        "Error 404: Heart completely overloaded with love! 💻❤️",
        "Yay! Let's celebrate with snacks later. 🍕",
        "You just locked in your forever best friend. 🔒💖",
        "My smile is officially permanent now! 😁",
        "Can we freeze this moment forever? ❄️✨",
        "You hold the key to my heart, always. 🔑",
        "Life is just better when we are a team. 🧑‍🤝‍🧑",
        "I love you more than words can ever describe! 📚💞",
        "Cue the romantic movie music! 🎬🎻",
        "You make my world infinitely brighter. ☀️",
        "Fairytales do exist, and you're mine. 🏰",
        "I'm totally doing a happy dance right now! 💃🕺",
        "You are the best thing that ever happened to me. 🌟",
    ]

    # --- SURPRISE FULL-SCREEN FLASH OVERLAY ---
    surprise_overlay = ft.Container(
        content=ft.Column(
            [
                ft.Text("💋", size=200),
                ft.Text("MUAAAAAAAAA!", size=50, weight=ft.FontWeight.BOLD, color="#d63384")
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        alignment=ft.Alignment.CENTER,
        expand=True,
        visible=False,  # Hidden by default
    )

    title_text = ft.Text(
        "Will you be my forever?",
        size=28,
        weight=ft.FontWeight.BOLD,
        color="#d63384",
        text_align=ft.TextAlign.CENTER,
    )

    counter_text = ft.Text(
        f"We have been smiling together for {days_together} days! 💕",
        size=16,
        color="#6c757d",
        text_align=ft.TextAlign.CENTER,
    )

    # Track how many times "Yes" has been clicked
    click_count = 0

    async def say_yes(e):
        nonlocal click_count
        click_count += 1

        if click_count == 1:
            # First Click: Play audio, show kiss flash, then show random response
            await audio.play()

            card_content.visible = False
            surprise_overlay.visible = True
            page.update()

            await asyncio.sleep(1.5)

            title_text.value = "Yaaay! 🥰"
            counter_text.value = random.choice(romantic_responses)
            no_button.visible = False
            yes_button.scale = 1.2

            surprise_overlay.visible = False
            card_content.visible = True
            page.update()

        elif click_count >= 2:
            # Second Click: Play audio, show the final message, then clear screen
            await audio.play()

            title_text.value = "ይኣክለኪ ከኣ ገጽ ርኢኪ  \n ስስስስስዲዲዲዲ \n Go Back To Work"
            counter_text.value = ""#"❤️"
            yes_button.visible = False
            no_button.visible = False

            surprise_overlay.visible = False
            card_content.visible = True
            page.update()

            # Wait 5 seconds so the message can be read, then leave only the background
            await asyncio.sleep(5.0)
            
            page.clean()
            page.update()

    def move_no(e):
        current_top = no_button.top if no_button.top is not None else 0
        current_left = no_button.left if no_button.left is not None else 120

        no_button.top = (current_top + 40) % 100
        no_button.left = (current_left + 60) % 240
        page.update()

    yes_button = ft.Button(
        content=ft.Text("Yes! ❤️", color=ft.Colors.WHITE, size=16),
        on_click=say_yes,
        style=ft.ButtonStyle(bgcolor="#e83e8c"),
        top=0,
        left=0,
    )

    no_button = ft.Button(
        content=ft.Text("No", color=ft.Colors.WHITE, size=16),
        on_hover=move_no,
        style=ft.ButtonStyle(bgcolor="#6c757d"),
        top=0,
        left=120,
    )

    button_area = ft.Stack(
        controls=[yes_button, no_button],
        width=240,
        height=150,
    )

    card_content = ft.Container(
        content=ft.Column(
            [
                ft.Icon(ft.Icons.FAVORITE, color="#e83e8c", size=50),
                title_text,
                counter_text,
                ft.Divider(height=20, color="transparent"),
                button_area,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        padding=40,
        bgcolor=ft.Colors.WHITE,
        border_radius=20,
        width=400,
        shadow=ft.BoxShadow(
            blur_radius=15,
            spread_radius=5,
            color="#f5c6cb",
        ),
        visible=True,
    )

    # Add both elements to the page at startup
    page.add(surprise_overlay, card_content)


# Launch in browser and tell Flet where to serve the "assets" folder
ft.run(main, assets_dir="assets")