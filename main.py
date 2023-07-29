# import streamlit as st


# def main():
#     st.title("Simple Website with Menu")

#     st.sidebar.title("Menu")
#     pages = ["Home", "Support", "Privacy Policy", "Terms and Conditions"]
#     selected_page = st.sidebar.selectbox("Select a category", pages)

#     if selected_page == "Home":
#         st.write("Welcome to the Home page!")
#         st.write("Here you can add the main content of your website.")
#     elif selected_page == "Support":
#         st.write("This is the Support page.")
#         st.write("You can provide information about how users can get support here.")
#     elif selected_page == "Privacy Policy":
#         st.write("This is the Privacy Policy page.")
#         st.write("You can provide your website's privacy policy here.")
#     elif selected_page == "Terms and Conditions":
#         st.write("This is the Terms and Conditions page.")
#         st.write("You can provide your website's terms and conditions here.")


# if __name__ == "__main__":
#     main()

import streamlit as st

# Support Page

def section1():
    st.header("KidCare Privacy Policy")

    st.write("Effective Date: 28.07.2023")
    st.write("Welcome to KidCare!")

    st.write("KidCare (the 'App') is a parenting application that provides access to a range of tools and features to support parents in their parenting journey. I value your privacy and am dedicated to protecting your personal information.")
    st.write("This Privacy Policy outlines how I collect, use, disclose, and store your information when you use our App.")
    st.subheader("Your Consent")
    st.write("By accessing and using the App, you consent to the collection, use, disclosure, storage, and processing of your information as outlined in this Privacy Policy.")

    st.subheader("Updates to the Policy")
    st.write("KidCare may update or modify this Privacy Policy from time to time, with or without prior notice to users. Users are bound by the Privacy Policy in effect at the time of using the App.")

    st.subheader("Information We Collect")
    st.write("I highly prioritize your privacy and ensure that I only collect the minimum necessary information to provide our services effectively. The information I collect may include:")
    st.write("1. Account Information: When you create a KidCare account, I may collect your name, email address, and other relevant account details.")
    st.write("2. Usage Data: I may collect usage data related to your interaction with the App, such as the features you use, the content you access, and your preferences.")
    st.write("3. Device Information: I may collect information about your device, including the device type, operating system, and unique device identifiers.")
    st.write("4. Communications: If you reach out to my support team or communicate with me through email or other channels, I may collect and store those communications for quality assurance and support purposes.")

    st.subheader("Use of Third-Party Services")
    st.write("KidCare utilizes third-party services, including Firebase by Google, for app analytics and functionality enhancement. Please note that these third-party services may collect certain information, but they do not have access to any of your personal details.")

    st.subheader("How I Use Your Information")
    st.write("KidCare uses your information for the following purposes:")
    st.write("1. Personalization: I use your information to personalize your experience within the App, providing content and features relevant to your preferences.")
    st.write("2. Communication: I may use your email address to send you important updates, notifications, and information related to the App.")
    st.write("3. Improvements: Your feedback and usage data help me enhance and improve the App's functionality and user experience.")
    st.write("4. Support: I may use your information to address your inquiries, provide technical support, and assist you with any issues related to the App.")

    st.subheader("Data Security and Confidentiality")
    st.write("KidCare takes data security seriously and employs industry-standard measures to protect your information from unauthorized access, disclosure, or alteration. I do not sell or share your personal information with third parties.")

    st.subheader("Unanswered Questions")
    st.write("If you have any unanswered questions or concerns regarding your privacy, kindly contact me at akbala20042020@mail.ru, and I will be delighted to assist you.")

    st.write("Thank you for choosing KidCare! I am committed to providing you with a safe, enjoyable, and rewarding parenting experience through my App.")


def section2():
    st.header("KidCare Terms and Conditions")
    
    st.write("Effective Date: 28.07.2023")
    st.write("Welcome to KidCare!")

    st.write("By using this app, you agree to be bound by these terms and conditions. If you do not agree with any part of these terms and conditions, please refrain from using KidCare.")

    st.subheader("License")
    st.write("KidCare is an indie-developed app, and all intellectual property rights for its material are owned by the developer. All rights are reserved, and users may only access and use KidCare for personal use, subject to the restrictions set in these terms and conditions.")

    st.write("You must not:")
    st.write("1. Republish material from KidCare.")
    st.write("2. Sell, rent, or sub-license material from KidCare.")
    st.write("3. Reproduce, duplicate, or copy material from KidCare.")
    st.write("4. Redistribute content from KidCare.")

    st.write("This Agreement shall begin on the date hereof.")

    st.subheader("Comments and User-Generated Content")
    st.write("KidCare may offer an opportunity for users to post comments and exchange opinions and information.")
    st.write("The developer does not filter, edit, publish, or review comments prior to their presence on the app. Comments reflect the views and opinions of the users and not necessarily those of the developer.")
    st.write("The developer shall not be liable for any comments or any liability, damages, or expenses caused and/or suffered as a result of any use of and/or posting of and/or appearance of the comments on this app.")

    st.write("The developer reserves the right to monitor all comments and to remove any comments that are considered inappropriate, offensive, or violate these terms and conditions.")

    st.write("By posting comments on KidCare, users warrant and represent that:")
    st.write("1. They are entitled to post the comments and have all necessary licenses and consents to do so.")
    st.write("2. The comments do not invade any intellectual property right, including without limitation copyright, patent, or trademark of any third party.")
    st.write("3. The comments do not contain any defamatory, libelous, offensive, indecent, or otherwise unlawful material which is an invasion of privacy.")
    st.write("4. The comments will not be used to solicit or promote business or present commercial activities or unlawful activity.")

    st.write("Users hereby grant the developer a non-exclusive license to use, reproduce, edit, and authorize others to use, reproduce, and edit any of their comments in any and all forms, formats, or media.")

    st.subheader("Hyperlinking to KidCare")
    st.write("Third-party organizations may link to KidCare without prior written approval, provided they adhere to the following conditions:")
    st.write("1. The link is not in any way deceptive.")
    st.write("2. The link does not falsely imply sponsorship, endorsement, or approval of the linking party and its products and/or services.")
    st.write("3. The link fits within the context of the linking party’s site.")

    st.write("The developer may consider and approve other link requests from the following types of organizations:")
    st.write("1. Commonly-known consumer and/or business information sources.")
    st.write("2. Associations or other groups representing charities.")
    st.write("3. Educational institutions and trade associations.")

    st.write("The developer will approve link requests if:")
    st.write("1. The link would not make the developer look unfavorably to itself or to its users.")
    st.write("2. The organization does not have any negative records with the developer.")
    st.write("3. The benefit to the developer from the visibility of the hyperlink compensates the absence of KidCare.")
    st.write("4. The link is in the context of general resource information.")

    st.write("Approved organizations may hyperlink to KidCare as follows:")
    st.write("1. By use of the developer's corporate name.")
    st.write("2. By use of the uniform resource locator being linked to.")
    st.write("3. By use of any other description of KidCare being linked to that makes sense within the context and format of content on the linking party’s site.")

    st.write("No use of the developer's logo or other artwork will be allowed for linking absent a trademark license agreement.")

    st.subheader("iFrames")
    st.write("Without prior approval and written permission, users may not create frames around KidCare's webpages that alter in any way the visual presentation or appearance of the app.")

    st.subheader("Content Liability")
    st.write("The developer shall not be held responsible for any content that appears on users' apps. Users agree to protect and defend the developer against all claims that are rising on KidCare.")
    st.write("No link(s) should appear on any website that may be interpreted as libelous, obscene, or criminal or which infringes, otherwise violates, or advocates the infringement or other violation of, any third-party rights.")

    st.subheader("Your Privacy")
    st.write("Please read our Privacy Policy for details on how we handle your personal information.")

    st.subheader("Reservation of Rights")
    st.write("The developer reserves the right to request that users remove all links or any particular link to KidCare. Users approve to immediately remove all links to KidCare upon request.")
    st.write("The developer also reserves the right to amend these terms and conditions and its linking policy at any time. By continuously linking to KidCare, users agree to be bound by and follow these linking terms and conditions.")

    st.subheader("Disclaimer")
    st.write("To the maximum extent permitted by applicable law, the developer excludes all representations, warranties, and conditions relating to KidCare and the use of this website. Nothing in this disclaimer will:")
    st.write("1. Limit or exclude the developer's or users' liability for death or personal injury.")
    st.write("2. Limit or exclude the developer's or users' liability for fraud or fraudulent misrepresentation.")
    st.write("3. Limit any of the developer's or users' liabilities in any way that is not permitted under applicable law.")
    st.write("4. Exclude any of the developer's or users' liabilities that may not be excluded under applicable law.")

    st.write("The limitations and prohibitions of liability set in this section and elsewhere in this disclaimer: ")
    st.write("(a) are subject to the preceding paragraph; and (b) govern all liabilities arising under the disclaimer, including liabilities arising in contract, in tort, and for breach of statutory duty.")

    st.write("As long as KidCare and the information and services on KidCare are provided free of charge, the developer will not be liable for any loss or damage of any nature.")


def section3():
    st.header("KidCare Support")

    # Contact Us
    st.subheader("Contact Us")
    st.write("If you need help or have any inquiries, please don't hesitate to reach out to dedicated support team."
             "You can contact me through the following channel:")
    st.write("**Email:** Send me an email at akbala20042020@mail.ru, and i will get back to you as soon as possible.")

# # Main app
# def main():
#     st.title("KidCare")
#     st.write("your faithful assistant in parenting! This is a unique application with a powerful AI assistant, created with love and care for the family. Get tips, play interactive games, read fairy tales and facilitate the path to understanding your child's world.")
#     # Add your menu here
#     menu = ["Privacy Policy", "Terms and Conditions", "Support"]
#     choice = st.sidebar.selectbox("Select a section", menu)

#     # Conditionally show the selected section
#     if choice == "Privacy Policy":
#         section1()
#     elif choice == "Terms and Conditions":
#         section2()
#     elif choice == "Support":
#         section3()

# if __name__ == "__main__":
#     main()
def main():
    st.title("KidCare")
    st.write("Your faithful assistant in parenting! This is a unique application with a powerful AI assistant, created with love and care for the family. Get tips, play interactive games, read fairy tales and facilitate the path to understanding your child's world.")

    # Define the URLs for each section
    section_urls = {
        'Privacy Policy': '/privacy',
        'Terms and Conditions': '/terms',
        'Support': '/support',
    }

    # Get the current request URL
    request_url = st.experimental_get_query_params().get('request', ['/'])[0]

    # Add your menu here
    menu = list(section_urls.keys())
    choice = st.sidebar.selectbox("Select a section", menu)

    # Determine the selected section URL
    selected_section_url = section_urls.get(choice, '/')

    # Check if the current request URL matches the selected section URL
    if request_url == selected_section_url:
        if choice == 'Privacy Policy':
            section1()
        elif choice == 'Terms and Conditions':
            section2()
        elif choice == 'Support':
            section3()
    else:
        # Show the default content or redirect to the selected section
        st.experimental_set_query_params(request=selected_section_url)
        st.experimental_rerun()

if __name__ == "__main__":
    main()