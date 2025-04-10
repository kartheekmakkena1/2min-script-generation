import streamlit as st
import time
import re
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
import time
geminiapi = "AIzaSyBoVGngmIYAKOLRzUYSRzAF6O4Oearqe78"  # Note: In production, store API keys securely
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite", api_key=geminiapi)
model1=ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite", api_key=geminiapi)

def main():
    # Configure the Streamlit page
    st.set_page_config(
        page_title="Script Generator",
        page_icon="🎬",
        layout="wide"
    )
    
    # Initialize session state variables if they don't exist
    if 'page' not in st.session_state:
        st.session_state.page = 'home'
    if 'generated_script' not in st.session_state:
        st.session_state.generated_script = ""
    if 'scenes' not in st.session_state:
        st.session_state.scenes = []
    if 'shots' not in st.session_state:
        st.session_state.shots = []
    
    # Display the appropriate page based on session state
    if st.session_state.page == 'home':
        display_home_page()
    elif st.session_state.page == 'script_editor':
        display_script_editor()
    elif st.session_state.page == 'scene_editor':
        display_scene_editor()
    elif st.session_state.page == 'shot_generator':
        display_shot_generator()
        
class shots(BaseModel):
    
    characters1: list[str] = Field(description='List the characters involved in this shot')
    narrative1: str = Field(description='you are a story teller give a 15-second narrative summary that Discribe the shot like explaining to a person in simple english.')  
    visual_description1: str = Field(description='Provide a highly detailed breakdown of the shot’s composition. Specify the key objects, characters, and environmental elements that will be prominently featured. Describe character movements, gestures, and expressions in this moment. Define the camera techniques used (angle, framing, depth of field, movement). Mention any significant visual effects, such as slow motion, lens flare, or CGI elements. Discuss how lighting, shadows, and reflections contribute to the visual storytelling.')  
    background1: str = Field(description='Describe the setting with rich sensory details but *don\'t include any character details*, including location, time of day, and weather conditions. Highlight architectural elements, props, and environmental textures that enhance the scene. Discuss the color palette, lighting intensity, and tonal mood that shape the scene’s atmosphere. Specify whether the background is static or dynamic, and if there are secondary elements such as moving crowds, flickering lights, or weather effects that add depth')  
    
    characters2: list[str] = Field(description='List the characters involved in this shot')
    narrative2: str = Field(description='you are a story teller give a 15-second narrative summary that Discribe the shot like explaining to a person in simple english..')  
    visual_description2: str = Field(description='Provide a highly detailed breakdown of the shot’s composition. Specify the key objects, characters, and environmental elements that will be prominently featured. Describe character movements, gestures, and expressions in this moment. Define the camera techniques used (angle, framing, depth of field, movement). Mention any significant visual effects, such as slow motion, lens flare, or CGI elements. Discuss how lighting, shadows, and reflections contribute to the visual storytelling.')  
    background2: str = Field(description='Describe the setting with rich sensory details but *don\'t include any character details*, including location, time of day, and weather conditions. Highlight architectural elements, props, and environmental textures that enhance the scene. Discuss the color palette, lighting intensity, and tonal mood that shape the scene’s atmosphere. Specify whether the background is static or dynamic, and if there are secondary elements such as moving crowds, flickering lights, or weather effects that add depth')  
    
    characters3: list[str] = Field(description='List the characters involved in this shot')
    narrative3: str = Field(description='you are a story teller give a 15-second narrative summary that Discribe the shot like explaining to a person in simple english..')  
    visual_description3: str = Field(description='Provide a highly detailed breakdown of the shot’s composition. Specify the key objects, characters, and environmental elements that will be prominently featured. Describe character movements, gestures, and expressions in this moment. Define the camera techniques used (angle, framing, depth of field, movement). Mention any significant visual effects, such as slow motion, lens flare, or CGI elements. Discuss how lighting, shadows, and reflections contribute to the visual storytelling.')  
    background3: str = Field(description='Describe the setting with rich sensory details but *don\'t include any character details*, including location, time of day, and weather conditions. Highlight architectural elements, props, and environmental textures that enhance the scene. Discuss the color palette, lighting intensity, and tonal mood that shape the scene’s atmosphere. Specify whether the background is static or dynamic, and if there are secondary elements such as moving crowds, flickering lights, or weather effects that add depth')  
   
    characters4: list[str] = Field(description='List the characters involved in this shot')
    narrative4: str = Field(description='you are a story teller give a 15-second narrative summary that Discribe the shot like explaining to a person in simple english..')  
    visual_description4: str = Field(description='Provide a highly detailed breakdown of the shot’s composition. Specify the key objects, characters, and environmental elements that will be prominently featured. Describe character movements, gestures, and expressions in this moment. Define the camera techniques used (angle, framing, depth of field, movement). Mention any significant visual effects, such as slow motion, lens flare, or CGI elements. Discuss how lighting, shadows, and reflections contribute to the visual storytelling.')  
    background4: str = Field(description='Describe the setting with rich sensory details but *don\'t include any character details*, including location, time of day, and weather conditions. Highlight architectural elements, props, and environmental textures that enhance the scene. Discuss the color palette, lighting intensity, and tonal mood that shape the scene’s atmosphere. Specify whether the background is static or dynamic, and if there are secondary elements such as moving crowds, flickering lights, or weather effects that add depth')  
  
    characters5: list[str] = Field(description='List the characters involved in this shot')
    narrative5: str = Field(description='you are a story teller give a 15-second narrative summary that Discribe the shot like explaining to a person in simple english.')  
    visual_description5: str = Field(description='Provide a highly detailed breakdown of the shot’s composition. Specify the key objects, characters, and environmental elements that will be prominently featured. Describe character movements, gestures, and expressions in this moment. Define the camera techniques used (angle, framing, depth of field, movement). Mention any significant visual effects, such as slow motion, lens flare, or CGI elements. Discuss how lighting, shadows, and reflections contribute to the visual storytelling.')  
    background5: str = Field(description='Describe the setting with rich sensory details but *don\'t include any character details*, including location, time of day, and weather conditions. Highlight architectural elements, props, and environmental textures that enhance the scene. Discuss the color palette, lighting intensity, and tonal mood that shape the scene’s atmosphere. Specify whether the background is static or dynamic, and if there are secondary elements such as moving crowds, flickering lights, or weather effects that add depth h')  


class Scene(BaseModel):    
    summary_and_progression: str = Field(description='give detailed discription of 2 lines  Construct a beat-by-beat architectural blueprint of the scene\'s dramatic machinery, identifying precise trigger points, progressive complications, false resolutions, mounting pressure tactics, revelation timing, emotional pivot moments, and aftermath consequences. Detail the strategic withholding and revealing of information to maximize tension, the specific pacing modulations that create emotional rhythm, and the mechanical connections between cause-and-effect chains. Map how power/knowledge/advantage shifts between characters at each turning point, how each beat recalibrates reader expectations, and how scene structure mirrors thematic elements through pattern and variation. Identify specific techniques of misdirection, foreshadowing, parallelism, or ironic contrast that enhance the scene\'s structural integrity and dramatic impact.')
    
    purpose_and_conflict: str = Field(description='give detailed discription of 2 lines  Construct a multilayered conflict ecosystem with precisely calibrated primary conflict (central problem demanding immediate resolution), secondary conflicts (complications arising from primary conflict), and tertiary conflicts (personal issues amplified by external pressure). Distinguish between visible conflicts (acknowledged obstacles) and invisible conflicts (unrecognized barriers, self-sabotage patterns). Detail how these conflicts intersect to create no-win scenarios, how tactical approaches to resolving one conflict exacerbate others, and how conflict resolution paradoxically creates new complications. Specify the psychological toll of each conflict type, their precise escalation mechanics, and how they force revealing character choices under specific types of pressure.')
    
    CharacterDevelopment: str = Field(description='give detailed discription of 2 lines  Diagram the precise architecture of character evolution through behavioral algorithms revealed under specific pressures. Catalog observable reaction patterns, speech cadences, physiological responses, decision-making filters, and defense mechanisms that constitute character. Map the character\'s position on key spectrums: vulnerability/guardedness, impulsivity/calculation, self-awareness/blindness, and emotional regulation/volatility. Detail the gap between self-perception and external perception, between stated values and demonstrated values. Identify threshold moments where character patterns break, revealing either deeper authentic layers or newly formed adaptations to trauma/success. Specify how secondary characters function as mirrors, contrasts, catalysts, or obstacles that illuminate protagonist development through interaction dynamics. Chart the precise movement along the character\'s transformational arc relative to their global journey.')
    
    SettingElements: str = Field(description='give detailed discription of 2 lines  Engineer a comprehensive environmental system functioning as both physical constraint architecture and psychological externalization. Detail precise geographical specifications (exact locations, distances, physical barriers, resource distribution, architectural features, population densities), environmental conditions (meteorological factors, seasonal influences, time-specific qualities of light, acoustic properties, olfactory elements), temporal frameworks (historical context, time compression/expansion techniques, deadline pressures, rhythmic elements), and cultural matrices (social norms, power hierarchies, economic factors, technological limitations/affordances). Map how these elements function as: plot enablers/limiters (creating specific action possibilities), character illuminators (reflecting or contrasting internal states), atmosphere generators (establishing precise emotional tones), symbolic systems (embodying thematic concerns), and narrative pace modulators. Identify how characters interact differently with identical environmental factors based on their specific psychological filters, how setting elements evolve throughout the scene to mirror emotional progression, and how the controlled revelation of setting details serves specific narrative functions.')
    
    narrativeVoice: str = Field(description='give detailed discription of 2 lines  Architect a comprehensive linguistic delivery system with precisely calibrated technical elements: sentence architecture (length variation patterns, structural diversity, rhythm creation through syntax manipulation), vocabulary distribution (register shifts, specialized terminology, connotative layers, etymology exploitation), figurative language deployment (metaphor systems, simile patterns, personification tactics, symbolism networks), narrative distance modulation (intimacy vs. detachment, filtration levels of character consciousness), psychic transparency control (thought revelation mechanisms, subtext communication systems), tonal orchestration (emotional colorings, ironic counterpoints, humor integration, gravitas establishment), sensory detail prioritization (which senses dominate description and when), and temporal manipulation (retrospection techniques, foreshadowing methods, pace control through language density). Identify how voice functions as characterization (revealing narrator psychology through linguistic choices), how it establishes genre expectations, how it creates reading experience through cognitive and emotional engagement patterns, how it strategically shifts in response to content intensity, and how it constructs thematic resonance through recurrent motifs, linguistic callbacks, and pattern establishment/disruption.')
 
    Characters: list[str] = Field(description='List the characters involved in this shot')
    
class StoryStructure2(BaseModel):
    characters: list[str] = Field(description='List of indian style character names and their detailed visual descriptions of physical appearance including **age**, **height**, **build**, **facial features**, **hair**, **eyes**, **skin tone**, **clothing style**')
    scene1: Scene = Field (description=(
            "The Beginning of Change: This scene introduces a turning point in the character’s life—a discovery, a challenge, "
            "or a shift in perspective that sets the story in motion. It takes place in a setting that enhances the moment, "
            "such as a quiet village square, a neon-lit city, a haunted mansion, or a futuristic spaceship. The protagonist "
            "notices something unusual—an object, an event, or a person—that forces them to react. Their decision to investigate, "
            "ignore, or flee will determine how the story unfolds. Potential elements include mysterious encounters, personal "
            "realizations, or the beginning of a larger mystery or adventure."
        ))
    

    scene2: Scene = Field(
        description=(
            "The Moment of Conflict: A situation arises that forces the protagonist into action—whether it be physical, emotional, "
            "or intellectual. The setting might be a courtroom, a battlefield, a locked room, or a high-tech lab, with environmental "
            "details like heavy rain, a ticking clock, or eerie silence adding to the tension. The protagonist faces an opponent, an "
            "obstacle, or an internal struggle that challenges their beliefs or skills. Their emotions shift—perhaps they grow desperate, "
            "find courage, or question everything they knew. The scene might involve betrayal, an unexpected ally, a mistake, or a crucial "
            "decision that changes everything."
        )
    )

    scene3: Scene = Field(
        description=(
            "The Consequences and Resolution: The protagonist faces the outcome of their choices and the aftermath of the central conflict. "
            "This could be in a hospital room, a battlefield, a prison, or a celebration hall, with the setting reflecting the mood—hope, "
            "loss, relief, or uncertainty. The protagonist may feel victorious, guilty, exhausted, or transformed. They must decide what comes "
            "next—whether to seek redemption, continue the fight, start anew, or live with their choices. Possible elements include a final "
            "twist, a hint at a larger mystery, or a quiet moment of reflection before moving forward."
        )
    )
    
class StoryStructure3(BaseModel):
    characters: list[str] = Field(description='List of indian style character names and their detailed visual descriptions of physical appearance including **age**, **height**, **build**, **facial features**, **hair**, **eyes**, **skin tone**, **clothing style**')
    scene1: Scene = Field(
        description=(
            "The Catalyst: This scene introduces the first major event that disrupts the protagonist’s normal life. "
            "It could be a discovery, an accident, a message, or a sudden realization. The setting plays a crucial role—"
            "it might be a quiet home, a busy city street, a deep forest, or an alien planet. The protagonist notices "
            "something unusual, and their reaction determines how the story unfolds. Potential elements include mysterious "
            "encounters, shocking news, or an opportunity they can’t ignore."
        )
    )

    scene2: Scene = Field(
        description=(
            "The Initial Struggle: The protagonist takes their first steps into the unknown, facing early challenges. "
            "They may struggle to adapt, make mistakes, or question their choices. The setting can be a training ground, "
            "a crime scene, a corporate office, or a magical realm. The protagonist starts encountering resistance—whether "
            "it’s an enemy, self-doubt, or unexpected consequences. This scene builds tension and gives hints about the bigger "
            "conflict ahead."
        )
    )

    scene3: Scene = Field(
        description=(
            "The Moment of Conflict: A major turning point where the protagonist faces a significant challenge, confrontation, "
            "or moral dilemma. This could be a battle, a betrayal, a dangerous revelation, or an internal crisis. The setting is "
            "dynamic—perhaps a courtroom, a battlefield, a deep-space station, or a high-stakes negotiation room. The protagonist "
            "makes a crucial decision that has lasting consequences, shifting their mindset and driving the story forward."
        )
    )

    scene4: Scene = Field(
        description=(
            "The Climax: The highest point of tension in the story. The protagonist faces their biggest obstacle—whether it’s a villain, "
            "a final test, or a personal revelation. The setting amplifies the intensity, such as a burning city, a collapsing dimension, "
            "a locked chamber, or an abandoned spaceship. The protagonist must make a decisive action that will determine their fate and "
            "the fate of those around them. This is where stakes are highest, emotions peak, and everything leads to a defining moment."
        )
    )

    scene5: Scene = Field(
        description=(
            "The Resolution: The protagonist deals with the aftermath of their journey. The setting might be a ruined battlefield, a courtroom, "
            "a farewell at a train station, or a moment of solitude under the stars. They reflect on what they’ve lost, gained, and how they’ve "
            "changed. Loose ends may be tied up, or a final twist could leave the audience wondering about what’s next. The resolution sets the tone "
            "for the ending—whether it’s hopeful, tragic, open-ended, or a setup for a sequel."
        )
    )
class StoryStructure5(BaseModel):
    characters: list[str] = Field(description='List of indian style character names and their detailed visual descriptions of physical appearance including **age**, **height**, **build**, **facial features**, **hair**, **eyes**, **skin tone**, **clothing style**')
    scene1: Scene = Field(
        description=(
            "The Ordinary World & Catalyst: The protagonist's normal life is introduced, setting the stage for their journey. "
            "This could be a peaceful village, a high-tech lab, a dystopian city, or a mysterious past. Suddenly, an inciting incident—"
            "a discovery, a message, or a personal loss—disrupts their world, forcing them to react. This event sparks the need for change."
        )
    )

    scene2: Scene = Field(
        description=(
            "The Call to Adventure: The protagonist faces a decision—ignore the disruption or take action. They may be hesitant, afraid, "
            "or skeptical. This scene might feature a mentor, an invitation, or a growing realization that they must leave their comfort zone. "
            "The world expands, revealing new opportunities, dangers, or mysteries."
        )
    )

    scene3: Scene = Field(
        description=(
            "The First Challenges: The protagonist begins their journey but struggles with their new reality. They face small obstacles that "
            "test their skills, beliefs, or willpower. They may meet allies, rivals, or unexpected enemies. The setting could be a dense jungle, "
            "a corporate boardroom, a supernatural realm, or a secret underground society. Tension builds as they realize what’s at stake."
        )
    )

    scene4: Scene = Field(
        description=(
            "The Midpoint Crisis: A major revelation or turning point occurs that changes the protagonist's understanding of their situation. "
            "They may uncover a hidden truth, suffer a painful loss, or realize their initial assumptions were wrong. The setting amplifies the mood—"
            "perhaps a crumbling castle, a tense negotiation table, a spaceship on the verge of collapse, or a sacred temple. The stakes are raised."
        )
    )

    scene5: Scene = Field(
        description=(
            "The Deepest Struggle: The protagonist faces their most personal conflict, whether it’s fear, betrayal, self-doubt, or physical danger. "
            "This could be a confrontation with their greatest enemy, a personal failure, or a shocking twist that leaves them at their lowest point. "
            "The setting reflects this intensity—stormy weather, an abandoned city, a high-security prison, or a shattered dream. They must either give up "
            "or find the strength to continue."
        )
    )

    scene6: Scene = Field(
        description=(
            "The Final Battle Begins: The protagonist gathers their resolve and prepares for the ultimate challenge. Allies may join, secrets may be "
            "revealed, and a sense of urgency pushes them forward. The setting could be a war-torn battlefield, a courtroom, a cybernetic wasteland, or "
            "a mystical realm on the brink of collapse. The climax is near, and all paths converge here."
        )
    )

    scene7: Scene = Field(
        description=(
            "The Climax: The most intense moment of the story, where the protagonist faces their greatest challenge head-on. They must overcome their fears, "
            "outsmart their enemy, or make a life-altering choice. The setting is dramatic—an erupting volcano, a crumbling kingdom, a high-speed chase, or "
            "a final emotional showdown. The outcome determines everything."
        )
    )

    scene8: Scene = Field(
        description=(
            "The Aftermath & Resolution: The dust settles, and the protagonist faces the consequences of their actions. The world may be forever changed, "
            "or they may return home, forever different. The setting could be a graveyard, a celebration hall, a quiet sunrise, or a prison cell. Loose ends "
            "are tied up, lessons are learned, and the story either concludes or hints at a new beginning."
        )
    )
class background(BaseModel):
    background : str =Field(description="this is description of a scene and i want to generate a background image with out characters do give detailed background description from this scene with out involving characters")
    
structured_model1= model.with_structured_output(shots)

structured_model2=model.with_structured_output(background)
def display_home_page():
    st.title("🎬 Script Generator")
    st.subheader("Create your perfect script")
    
    with st.form("input_form"):
        # Text input for prompt
        prompt = st.text_area("Enter your script prompt:", height=150, 
                             placeholder="Example: A comedy scene between two friends discussing their weekend plans...")
        
        # Create columns for dropdown selections
        col1, col2, col3 = st.columns(3)
        
        with col1:
            speaker = st.selectbox(
                "Select Speaker:",
                ["Male Adult", "Female Adult", "Child", "Multiple Characters", "Narrator"]
            )
        
        with col2:
            duration = st.selectbox(
                "Select Duration:",
                ["2 minutes", "3 minutes", "5 minutes"]
            )
        
        with col3:
            style = st.selectbox(
                "Select Style:",
                ["cartoon", "Indian", "Cyberpunk", "anime", "Dark", "ghibli "]
            )
        
        # Submit button
        submit = st.form_submit_button("Generate Script")
        
        if submit:
            with st.spinner("Generating your script..."):
                # Simulate API call or processing time
                time.sleep(2)
                

                st.session_state.generated_script = generate_sample_script(prompt, speaker, duration, style)
                

                st.session_state.scenes = split_script_into_scenes(st.session_state.generated_script,duration)
                st.session_state.duretion=duration
                st.session_state.page = 'script_editor'
                st.rerun()

def display_script_editor():
    st.title("📝 Full Script Editor")
    calll()
    for i,scene in enumerate(st.session_state.sceness,1):
        with st.expander(f"Scene {i}", expanded=True):
            # Summary and Progression
            
            scene.summary_and_progression = st.text_area(
                "Edit Summary and Progression",
                value=scene.summary_and_progression,
                height=100,
                key=f"scene{i}_summary_and_progression"
            )
    # Create columns for buttons
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("⬅️ Back to Generator"):
            st.session_state.page = 'home'
            st.rerun()
    
    with col2:
        if st.button("🔄 Regenerate Script"):
            with st.spinner("Regenerating..."):
                time.sleep(1)
                st.session_state.scenes = split_script_into_scenes(st.session_state.generated_script,st.session_state.duretion)
                st.rerun()
    
    with col3:
        if st.button("✏️ Edit Scene by Scene"):
            # Split the script into scenes again in case it was modified
            st.session_state.page = 'scene_editor'
            st.rerun()
    
    with col4:
        if st.button("➡️ Proceed to Shot-wise Generation"):
            with st.spinner("Preparing shot breakdown..."):
                time.sleep(1)
                st.session_state.shott=create_sample_shots()
                # Create sample shots from the script
                st.session_state.page = 'shot_generator'
                st.rerun()

def display_scene_editor():
    st.title("🎭 Scene by Scene Editor")
    
    for i,scene in enumerate(st.session_state.sceness,1):
        with st.expander(f"Scene {i}", expanded=True):
            # Summary and Progression
            scene.summary_and_progression = st.text_area(
                "Edit Summary and Progression",
                value=scene.summary_and_progression,
                height=100,
                key=f"scene{i}_summary_and_progression"
            )

            # Purpose and Conflict
            scene.purpose_and_conflict = st.text_area(
                "Edit Purpose and Conflict",
                value=scene.purpose_and_conflict,
                height=100,
                key=f"scene{i}_purpose_and_conflict"
            )

            # Character Development
            scene.CharacterDevelopment = st.text_area(
                "Edit Character Development",
                value=scene.CharacterDevelopment,
                height=100,
                key=f"scene{i}_CharacterDevelopment"
            )

            # Setting Elements
            scene.SettingElements = st.text_area(
                "Edit Setting Elements",
                value=scene.SettingElements,
                height=100,
                key=f"scene{i}_SettingElements"
            )

            # Narrative Voice
            scene.narrativeVoice = st.text_area(
                "Edit Narrative Voice",
                value=scene.narrativeVoice,
                height=100,
                key=f"scene{i}_narrativeVoice"
            )
            
            # Characters
            scene.Characters = st.text_area(
                "Edit Characters",
                value=scene.Characters,
                height=100,
                key=f"scene{i}_Characters"
            )
                
    # Add a new scene button
    if st.button("➕ Add New Scene"):
        st.session_state.scenes.append("New scene description...")
        st.rerun()
    
    # Create columns for navigation buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("⬅️ Back to Full Script Editor"):
            st.session_state.page = 'script_editor'
            st.rerun()
    
    with col2:
        if st.button("➡️ Proceed to Shot-wise Generation"):
            with st.spinner("Preparing shot breakdown..."):
                time.sleep(1)
                st.session_state.shott=create_sample_shots()
                st.session_state.page = 'shot_generator'
                st.rerun()

def display_shot_generator():
    st.title("🎬 Shot-wise Breakdown")
    for i, scene in enumerate(st.session_state.shott, 1):
        with st.expander(f"Scene {i}", expanded=True):
            # Create tabs for the shots
            shot_tabs = st.tabs(["Shot 1", "Shot 2", "Shot 3", "Shot 4", "Shot 5","narration"])
            
            # Shot 1
            with shot_tabs[0]:
                scene.characters1 = st.text_area(
                    "Edit characters",
                    value=scene.characters1,
                    height=100,
                    key=f"scene{i}_shot1_characters"
                )
                scene.visual_description1 = st.text_area(
                    "Edit visual_description",
                    value=scene.visual_description1,
                    height=100,
                    key=f"scene{i}_shot1_visual_description"
                )
                scene.background1 = st.text_area(
                    "Edit background",
                    value=scene.background1,
                    height=100,
                    key=f"scene{i}_shot1_background"
                )
            
            # Shot 2
            with shot_tabs[1]:
                scene.characters2 = st.text_area(
                    "Edit characters",
                    value=scene.characters2,
                    height=100,
                    key=f"scene{i}_shot2_characters"
                )
                scene.visual_description2 = st.text_area(
                    "Edit visual_description",
                    value=scene.visual_description2,
                    height=100,
                    key=f"scene{i}_shot2_visual_description"
                )
                scene.background2 = st.text_area(
                    "Edit background",
                    value=scene.background2,
                    height=100,
                    key=f"scene{i}_shot2_background"
                )
            
            # Shot 3
            with shot_tabs[2]:
                scene.characters3 = st.text_area(
                    "Edit characters",
                    value=scene.characters3,
                    height=100,
                    key=f"scene{i}_shot3_characters"
                )
                scene.visual_description3 = st.text_area(
                    "Edit visual_description",
                    value=scene.visual_description3,
                    height=100,
                    key=f"scene{i}_shot3_visual_description"
                )
                scene.background3 = st.text_area(
                    "Edit background",
                    value=scene.background3,
                    height=100,
                    key=f"scene{i}_shot3_background"
                )
            
            # Shot 4
            with shot_tabs[3]:
                scene.characters4 = st.text_area(
                    "Edit characters",
                    value=scene.characters4,
                    height=100,
                    key=f"scene{i}_shot4_characters"
                )
                scene.visual_description4 = st.text_area(
                    "Edit visual_description",
                    value=scene.visual_description4,
                    height=100,
                    key=f"scene{i}_shot4_visual_description"
                )
                scene.background4 = st.text_area(
                    "Edit background",
                    value=scene.background4,
                    height=100,
                    key=f"scene{i}_shot4_background"
                )
            
            # Shot 5
            with shot_tabs[4]:
                scene.characters5 = st.text_area(
                    "Edit characters",
                    value=scene.characters5,
                    height=100,
                    key=f"scene{i}_shot5_characters"
                )
                scene.visual_description5 = st.text_area(
                    "Edit visual_description",
                    value=scene.visual_description5,
                    height=100,
                    key=f"scene{i}_shot5_visual_description"
                )
                scene.background5 = st.text_area(
                    "Edit background",
                    value=scene.background5,
                    height=100,
                    key=f"scene{i}_shot5_background"
                )
                with shot_tabs[5]:
                    if(i==1):
                        st.session_state.narration1 = st.text_area(
                            "Edit narration",
                            value=st.session_state.narration1,
                            height=100,
                            key=f"scene{i}_shot5_narration"
                        )
                    elif(i==2):
                        st.session_state.narration2 = st.text_area(
                            "Edit narration",
                            value=st.session_state.narration2,
                            height=100,
                            key=f"scene{i}_shot5_narration"
                        )
                    elif(i==3):
                        st.session_state.narration3 = st.text_area(
                            "Edit narration",
                            value=st.session_state.narration3,
                            height=100,
                            key=f"scene{i}_shot5_narration"
                        )
                    elif(i==4):
                        st.session_state.narration4 = st.text_area(
                            "Edit narration",
                            value=st.session_state.narration4,
                            height=100,
                            key=f"scene{i}_shot5_narration"
                        )
                    elif(i==5):
                        st.session_state.narration5 = st.text_area(
                            "Edit narration",
                            value=st.session_state.narration5,
                            height=100,
                            key=f"scene{i}_shot5_narration"
                        )
                    elif(i==6):
                        st.session_state.narration6 = st.text_area(
                            "Edit narration",
                            value=st.session_state.narration6,
                            height=100,
                            key=f"scene{i}_shot5_narration"
                        )
                    elif(i==7):
                        st.session_state.narration7 = st.text_area(
                            "Edit narration",
                            value=st.session_state.narration7,
                            height=100,
                            key=f"scene{i}_shot5_narration"
                        )
                    else:
                        st.session_state.narration8 = st.text_area(
                            "Edit narration",
                            value=st.session_state.narration8,
                            height=100,
                            key=f"scene{i}_shot5_narration"
                        )
  
    # Add a new shot button
    if st.button("➕ Add New Shot"):
        st.session_state.shots.append("New shot description...")
        st.rerun()
    
    # Create columns for navigation buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("⬅️ Back to Full Script Editor"):
            st.session_state.page = 'script_editor'
            st.rerun()
            
    with col2:
        if st.button("⬅️ Back to Scene Editor"):
            st.session_state.page = 'scene_editor'
            st.rerun()
    
    with col3:
        if st.button("💾 Save All Shots"):
            st.success("All shots saved successfully!")
            # In a real app, save the shots to a database or file

def split_script_into_scenes(script,duration):    
    if duration == "5 minutes":
        structured_model = model.with_structured_output(StoryStructure5)
        result = structured_model.invoke(script)
    elif duration == "3 minutes":
        structured_model = model.with_structured_output(StoryStructure3)
        result = structured_model.invoke(script)      
    else:
        structured_model = model.with_structured_output(StoryStructure2)
        result = structured_model.invoke(script)
    return result
def generate_sample_script(prompt, speaker, duration, style):
    # In a real app, this would call an AI model or API
    return f""" Generate a story in the {style.upper()} style  BASED ON: "{prompt}" EATURING: {speaker} DURATION: {duration}
    """
def create_sample_shots():
    if(st.session_state.duretion == "5 minutes"):
        st.session_state.scene1,st.session_state.narration1=print_scene(st.session_state.scenes.scene1)
        
        st.session_state.scene1.visual_description1 = st.session_state.scene1.visual_description1 + " AND " + st.session_state.scene1.background1
        st.session_state.scene1.background1 = structured_model2.invoke(st.session_state.scene1.background1).background

        st.session_state.scene1.visual_description2 = st.session_state.scene1.visual_description2 + " AND " + st.session_state.scene1.background2
        st.session_state.scene1.background2 = structured_model2.invoke(st.session_state.scene1.background2).background


        st.session_state.scene1.visual_description3 = st.session_state.scene1.visual_description3 + " AND " + st.session_state.scene1.background3
        st.session_state.scene1.background3 = structured_model2.invoke(st.session_state.scene1.background3).background


        st.session_state.scene1.visual_description4 = st.session_state.scene1.visual_description4 + " AND " + st.session_state.scene1.background4
        st.session_state.scene1.background4 = structured_model2.invoke(st.session_state.scene1.background4).background

        st.session_state.scene1.visual_description5 = st.session_state.scene1.visual_description5 + " AND " + st.session_state.scene1.background5
        st.session_state.scene1.background5 = structured_model2.invoke(st.session_state.scene1.background5).background  

        st.session_state.scene2,st.session_state.narration2=print_scene(st.session_state.scenes.scene2,st.session_state.scene1,st.session_state.narration1)
        

        st.session_state.scene2.visual_description1 = st.session_state.scene2.visual_description1 + " AND " + st.session_state.scene2.background1
        st.session_state.scene2.background1 = structured_model2.invoke(st.session_state.scene2.background1).background
        
        st.session_state.scene2.visual_description2 = st.session_state.scene2.visual_description2 + " AND " + st.session_state.scene2.background2
        st.session_state.scene2.background2 = structured_model2.invoke(st.session_state.scene2.background2).background
        
        st.session_state.scene2.visual_description3 = st.session_state.scene2.visual_description3 + " AND " + st.session_state.scene2.background3
        st.session_state.scene2.background3 = structured_model2.invoke(st.session_state.scene2.background3).background
        
        st.session_state.scene2.visual_description4 = st.session_state.scene2.visual_description4 + " AND " + st.session_state.scene2.background4
        st.session_state.scene2.background4 = structured_model2.invoke(st.session_state.scene2.background4).background
        
        st.session_state.scene2.visual_description5 = st.session_state.scene2.visual_description5 + " AND " + st.session_state.scene2.background5
        st.session_state.scene2.background5 = structured_model2.invoke(st.session_state.scene2.background5).background
        
        st.session_state.scene3,st.session_state.narration3=print_scene(st.session_state.scenes.scene3,st.session_state.scene2,st.session_state.narration2)
# Assign values individually first
        st.session_state.scene3.visual_description1 = st.session_state.scene3.visual_description1 + " AND " + st.session_state.scene3.background1
        st.session_state.scene3.background1 = structured_model2.invoke(st.session_state.scene3.background1).background
        
        st.session_state.scene3.visual_description2 = st.session_state.scene3.visual_description2 + " AND " + st.session_state.scene3.background2
        st.session_state.scene3.background2 = structured_model2.invoke(st.session_state.scene3.background2).background
        
        st.session_state.scene3.visual_description3 = st.session_state.scene3.visual_description3 + " AND " + st.session_state.scene3.background3
        st.session_state.scene3.background3 = structured_model2.invoke(st.session_state.scene3.background3).background
        
        st.session_state.scene3.visual_description4 = st.session_state.scene3.visual_description4 + " AND " + st.session_state.scene3.background4
        st.session_state.scene3.background4 = structured_model2.invoke(st.session_state.scene3.background4).background
        
        st.session_state.scene3.visual_description5 = st.session_state.scene3.visual_description5 + " AND " + st.session_state.scene3.background5
        st.session_state.scene3.background5 = structured_model2.invoke(st.session_state.scene3.background5).background
        
        st.session_state.scene4,st.session_state.narration4=print_scene(st.session_state.scenes.scene4,st.session_state.scene3,st.session_state.narration3)
# Assign values individually first
        st.session_state.scene4.visual_description1 = st.session_state.scene4.visual_description1 + " AND " + st.session_state.scene4.background1
        st.session_state.scene4.background1 = structured_model2.invoke(st.session_state.scene4.background1).background
        st.session_state.scene4.visual_description2 = st.session_state.scene4.visual_description2 + " AND " + st.session_state.scene4.background2
        st.session_state.scene4.background2 = structured_model2.invoke(st.session_state.scene4.background2).background
        
        st.session_state.scene4.visual_description3 = st.session_state.scene4.visual_description3 + " AND " + st.session_state.scene4.background3
        st.session_state.scene4.background3 = structured_model2.invoke(st.session_state.scene4.background3).background
        
        st.session_state.scene4.visual_description4 = st.session_state.scene4.visual_description4 + " AND " + st.session_state.scene4.background4
        st.session_state.scene4.background4 = structured_model2.invoke(st.session_state.scene4.background4).background
        
        st.session_state.scene4.visual_description5 = st.session_state.scene4.visual_description5 + " AND " + st.session_state.scene4.background5
        st.session_state.scene4.background5 = structured_model2.invoke(st.session_state.scene4.background5).background

        st.session_state.scene5,st.session_state.narration5=print_scene(st.session_state.scenes.scene5,st.session_state.scene4,st.session_state.narration4)
# Assign values individually first
        st.session_state.scene5.visual_description1 = st.session_state.scene5.visual_description1 + " AND " + st.session_state.scene5.background1
        st.session_state.scene5.background1 = structured_model2.invoke(st.session_state.scene5.background1).background
        
        st.session_state.scene5.visual_description2 = st.session_state.scene5.visual_description2 + " AND " + st.session_state.scene5.background2
        st.session_state.scene5.background2 = structured_model2.invoke(st.session_state.scene5.background2).background
        
        st.session_state.scene5.visual_description3 = st.session_state.scene5.visual_description3 + " AND " + st.session_state.scene5.background3
        st.session_state.scene5.background3 = structured_model2.invoke(st.session_state.scene5.background3).background
        
        st.session_state.scene5.visual_description4 = st.session_state.scene5.visual_description4 + " AND " + st.session_state.scene5.background4
        st.session_state.scene5.background4 = structured_model2.invoke(st.session_state.scene5.background4).background
        
        st.session_state.scene5.visual_description5 = st.session_state.scene5.visual_description5 + " AND " + st.session_state.scene5.background5
        st.session_state.scene5.background5 = structured_model2.invoke(st.session_state.scene5.background5).background

        st.session_state.scene6,st.session_state.narration6=print_scene(st.session_state.scenes.scene6,st.session_state.scene5,st.session_state.narration5)
# Assign values individually first
        st.session_state.scene6.visual_description1 = st.session_state.scene6.visual_description1 + " AND " + st.session_state.scene6.background1
        st.session_state.scene6.background1 = structured_model2.invoke(st.session_state.scene6.background1).background
        
        st.session_state.scene6.visual_description2 = st.session_state.scene6.visual_description2 + " AND " + st.session_state.scene6.background2
        st.session_state.scene6.background2 = structured_model2.invoke(st.session_state.scene6.background2).background
        
        st.session_state.scene6.visual_description3 = st.session_state.scene6.visual_description3 + " AND " + st.session_state.scene6.background3
        st.session_state.scene6.background3 = structured_model2.invoke(st.session_state.scene6.background3).background
        
        st.session_state.scene6.visual_description4 = st.session_state.scene6.visual_description4 + " AND " + st.session_state.scene6.background4
        st.session_state.scene6.background4 = structured_model2.invoke(st.session_state.scene6.background4).background
        
        st.session_state.scene6.visual_description5 = st.session_state.scene6.visual_description5 + " AND " + st.session_state.scene6.background5
        st.session_state.scene6.background5 = structured_model2.invoke(st.session_state.scene6.background5).background

        st.session_state.scene7,st.session_state.narration7=print_scene(st.session_state.scenes.scene7,st.session_state.scene6,st.session_state.narration6)
# Assign values individually first
        st.session_state.scene7.visual_description1 = st.session_state.scene7.visual_description1 + " AND " + st.session_state.scene7.background1
        st.session_state.scene7.background1 = structured_model2.invoke(st.session_state.scene7.background1).background
        
        st.session_state.scene7.visual_description2 = st.session_state.scene7.visual_description2 + " AND " + st.session_state.scene7.background2
        st.session_state.scene7.background2 = structured_model2.invoke(st.session_state.scene7.background2).background
        
        st.session_state.scene7.visual_description3 = st.session_state.scene7.visual_description3 + " AND " + st.session_state.scene7.background3
        st.session_state.scene7.background3 = structured_model2.invoke(st.session_state.scene7.background3).background
        
        st.session_state.scene7.visual_description4 = st.session_state.scene7.visual_description4 + " AND " + st.session_state.scene7.background4
        st.session_state.scene7.background4 = structured_model2.invoke(st.session_state.scene7.background4).background
        
        st.session_state.scene7.visual_description5 = st.session_state.scene7.visual_description5 + " AND " + st.session_state.scene7.background5
        st.session_state.scene7.background5 = structured_model2.invoke(st.session_state.scene7.background5).background
        
        st.session_state.scene8,st.session_state.narration8=print_scene(st.session_state.scenes.scene8,st.session_state.scene7,st.session_state.narration7)
# Assign values individually first
        st.session_state.scene8.visual_description1 = st.session_state.scene8.visual_description1 + " AND " + st.session_state.scene8.background1
        st.session_state.scene8.background1 = structured_model2.invoke(st.session_state.scene8.background1).background
        
        st.session_state.scene8.visual_description2 = st.session_state.scene8.visual_description2 + " AND " + st.session_state.scene8.background2
        st.session_state.scene8.background2 = structured_model2.invoke(st.session_state.scene8.background2).background
        
        st.session_state.scene8.visual_description3 = st.session_state.scene8.visual_description3 + " AND " + st.session_state.scene8.background3
        st.session_state.scene8.background3 = structured_model2.invoke(st.session_state.scene8.background3).background
        
        st.session_state.scene8.visual_description4 = st.session_state.scene8.visual_description4 + " AND " + st.session_state.scene8.background4
        st.session_state.scene8.background4 = structured_model2.invoke(st.session_state.scene8.background4).background
        
        st.session_state.scene8.visual_description5 = st.session_state.scene8.visual_description5 + " AND " + st.session_state.scene8.background5
        st.session_state.scene8.background5 = structured_model2.invoke(st.session_state.scene8.background5).background
        
        generatedscript=[
        st.session_state.scene1, st.session_state.scene2, st.session_state.scene3,st.session_state.scene4,st.session_state.scene5,st.session_state.scene6,st.session_state.scene7,st.session_state.scene8
            ]     
    elif(st.session_state.duretion == "3 minutes"):
        st.session_state.scene1,st.session_state.narration1=print_scene(st.session_state.scenes.scene1)
        
        st.session_state.scene1.visual_description1 = st.session_state.scene1.visual_description1 + " AND " + st.session_state.scene1.background1
        st.session_state.scene1.background1 = structured_model2.invoke(st.session_state.scene1.background1).background

        st.session_state.scene1.visual_description2 = st.session_state.scene1.visual_description2 + " AND " + st.session_state.scene1.background2
        st.session_state.scene1.background2 = structured_model2.invoke(st.session_state.scene1.background2).background


        st.session_state.scene1.visual_description3 = st.session_state.scene1.visual_description3 + " AND " + st.session_state.scene1.background3
        st.session_state.scene1.background3 = structured_model2.invoke(st.session_state.scene1.background3).background


        st.session_state.scene1.visual_description4 = st.session_state.scene1.visual_description4 + " AND " + st.session_state.scene1.background4
        st.session_state.scene1.background4 = structured_model2.invoke(st.session_state.scene1.background4).background

        st.session_state.scene1.visual_description5 = st.session_state.scene1.visual_description5 + " AND " + st.session_state.scene1.background5
        st.session_state.scene1.background5 = structured_model2.invoke(st.session_state.scene1.background5).background  

        st.session_state.scene2,st.session_state.narration2=print_scene(st.session_state.scenes.scene2,st.session_state.scene1,st.session_state.narration1)
        

        st.session_state.scene2.visual_description1 = st.session_state.scene2.visual_description1 + " AND " + st.session_state.scene2.background1
        st.session_state.scene2.background1 = structured_model2.invoke(st.session_state.scene2.background1).background
        
        st.session_state.scene2.visual_description2 = st.session_state.scene2.visual_description2 + " AND " + st.session_state.scene2.background2
        st.session_state.scene2.background2 = structured_model2.invoke(st.session_state.scene2.background2).background
        
        st.session_state.scene2.visual_description3 = st.session_state.scene2.visual_description3 + " AND " + st.session_state.scene2.background3
        st.session_state.scene2.background3 = structured_model2.invoke(st.session_state.scene2.background3).background
        
        st.session_state.scene2.visual_description4 = st.session_state.scene2.visual_description4 + " AND " + st.session_state.scene2.background4
        st.session_state.scene2.background4 = structured_model2.invoke(st.session_state.scene2.background4).background
        
        st.session_state.scene2.visual_description5 = st.session_state.scene2.visual_description5 + " AND " + st.session_state.scene2.background5
        st.session_state.scene2.background5 = structured_model2.invoke(st.session_state.scene2.background5).background
        
        st.session_state.scene3,st.session_state.narration3=print_scene(st.session_state.scenes.scene3,st.session_state.scene2,st.session_state.narration2)
# Assign values individually first
        st.session_state.scene3.visual_description1 = st.session_state.scene3.visual_description1 + " AND " + st.session_state.scene3.background1
        st.session_state.scene3.background1 = structured_model2.invoke(st.session_state.scene3.background1).background
        
        st.session_state.scene3.visual_description2 = st.session_state.scene3.visual_description2 + " AND " + st.session_state.scene3.background2
        st.session_state.scene3.background2 = structured_model2.invoke(st.session_state.scene3.background2).background
        
        st.session_state.scene3.visual_description3 = st.session_state.scene3.visual_description3 + " AND " + st.session_state.scene3.background3
        st.session_state.scene3.background3 = structured_model2.invoke(st.session_state.scene3.background3).background
        
        st.session_state.scene3.visual_description4 = st.session_state.scene3.visual_description4 + " AND " + st.session_state.scene3.background4
        st.session_state.scene3.background4 = structured_model2.invoke(st.session_state.scene3.background4).background
        
        st.session_state.scene3.visual_description5 = st.session_state.scene3.visual_description5 + " AND " + st.session_state.scene3.background5
        st.session_state.scene3.background5 = structured_model2.invoke(st.session_state.scene3.background5).background
        
        st.session_state.scene4,st.session_state.narration4=print_scene(st.session_state.scenes.scene4,st.session_state.scene3,st.session_state.narration3)
# Assign values individually first
        st.session_state.scene4.visual_description1 = st.session_state.scene4.visual_description1 + " AND " + st.session_state.scene4.background1
        st.session_state.scene4.background1 = structured_model2.invoke(st.session_state.scene4.background1).background
        st.session_state.scene4.visual_description2 = st.session_state.scene4.visual_description2 + " AND " + st.session_state.scene4.background2
        st.session_state.scene4.background2 = structured_model2.invoke(st.session_state.scene4.background2).background
        
        st.session_state.scene4.visual_description3 = st.session_state.scene4.visual_description3 + " AND " + st.session_state.scene4.background3
        st.session_state.scene4.background3 = structured_model2.invoke(st.session_state.scene4.background3).background
        
        st.session_state.scene4.visual_description4 = st.session_state.scene4.visual_description4 + " AND " + st.session_state.scene4.background4
        st.session_state.scene4.background4 = structured_model2.invoke(st.session_state.scene4.background4).background
        
        st.session_state.scene4.visual_description5 = st.session_state.scene4.visual_description5 + " AND " + st.session_state.scene4.background5
        st.session_state.scene4.background5 = structured_model2.invoke(st.session_state.scene4.background5).background

        st.session_state.scene5,st.session_state.narration5=print_scene(st.session_state.scenes.scene5,st.session_state.scene4,st.session_state.narration4)
# Assign values individually first
        st.session_state.scene5.visual_description1 = st.session_state.scene5.visual_description1 + " AND " + st.session_state.scene5.background1
        st.session_state.scene5.background1 = structured_model2.invoke(st.session_state.scene5.background1).background
        
        st.session_state.scene5.visual_description2 = st.session_state.scene5.visual_description2 + " AND " + st.session_state.scene5.background2
        st.session_state.scene5.background2 = structured_model2.invoke(st.session_state.scene5.background2).background
        
        st.session_state.scene5.visual_description3 = st.session_state.scene5.visual_description3 + " AND " + st.session_state.scene5.background3
        st.session_state.scene5.background3 = structured_model2.invoke(st.session_state.scene5.background3).background
        
        st.session_state.scene5.visual_description4 = st.session_state.scene5.visual_description4 + " AND " + st.session_state.scene5.background4
        st.session_state.scene5.background4 = structured_model2.invoke(st.session_state.scene5.background4).background
        
        st.session_state.scene5.visual_description5 = st.session_state.scene5.visual_description5 + " AND " + st.session_state.scene5.background5
        st.session_state.scene5.background5 = structured_model2.invoke(st.session_state.scene5.background5).background
        
        generatedscript =[
        st.session_state.scene1, st.session_state.scene2, st.session_state.scene3,st.session_state.scene4,st.session_state.scene5
            ]   
    else:
        st.session_state.scene1,st.session_state.narration1=print_scene(st.session_state.scenes.scene1)
        
        st.session_state.scene1.visual_description1 = st.session_state.scene1.visual_description1 + " AND " + st.session_state.scene1.background1
        st.session_state.scene1.background1 = structured_model2.invoke(st.session_state.scene1.background1).background

        st.session_state.scene1.visual_description2 = st.session_state.scene1.visual_description2 + " AND " + st.session_state.scene1.background2
        st.session_state.scene1.background2 = structured_model2.invoke(st.session_state.scene1.background2).background


        st.session_state.scene1.visual_description3 = st.session_state.scene1.visual_description3 + " AND " + st.session_state.scene1.background3
        st.session_state.scene1.background3 = structured_model2.invoke(st.session_state.scene1.background3).background


        st.session_state.scene1.visual_description4 = st.session_state.scene1.visual_description4 + " AND " + st.session_state.scene1.background4
        st.session_state.scene1.background4 = structured_model2.invoke(st.session_state.scene1.background4).background

        st.session_state.scene1.visual_description5 = st.session_state.scene1.visual_description5 + " AND " + st.session_state.scene1.background5
        st.session_state.scene1.background5 = structured_model2.invoke(st.session_state.scene1.background5).background  

        st.session_state.scene2,st.session_state.narration2=print_scene(st.session_state.scenes.scene2,st.session_state.scene1,st.session_state.narration1)
        

        st.session_state.scene2.visual_description1 = st.session_state.scene2.visual_description1 + " AND " + st.session_state.scene2.background1
        st.session_state.scene2.background1 = structured_model2.invoke(st.session_state.scene2.background1).background
        
        st.session_state.scene2.visual_description2 = st.session_state.scene2.visual_description2 + " AND " + st.session_state.scene2.background2
        st.session_state.scene2.background2 = structured_model2.invoke(st.session_state.scene2.background2).background
        
        st.session_state.scene2.visual_description3 = st.session_state.scene2.visual_description3 + " AND " + st.session_state.scene2.background3
        st.session_state.scene2.background3 = structured_model2.invoke(st.session_state.scene2.background3).background
        
        st.session_state.scene2.visual_description4 = st.session_state.scene2.visual_description4 + " AND " + st.session_state.scene2.background4
        st.session_state.scene2.background4 = structured_model2.invoke(st.session_state.scene2.background4).background
        
        st.session_state.scene2.visual_description5 = st.session_state.scene2.visual_description5 + " AND " + st.session_state.scene2.background5
        st.session_state.scene2.background5 = structured_model2.invoke(st.session_state.scene2.background5).background
        
        st.session_state.scene3,st.session_state.narration3=print_scene(st.session_state.scenes.scene3,st.session_state.scene2,st.session_state.narration2)
# Assign values individually first
        st.session_state.scene3.visual_description1 = st.session_state.scene3.visual_description1 + " AND " + st.session_state.scene3.background1
        st.session_state.scene3.background1 = structured_model2.invoke(st.session_state.scene3.background1).background
        
        st.session_state.scene3.visual_description2 = st.session_state.scene3.visual_description2 + " AND " + st.session_state.scene3.background2
        st.session_state.scene3.background2 = structured_model2.invoke(st.session_state.scene3.background2).background
        
        st.session_state.scene3.visual_description3 = st.session_state.scene3.visual_description3 + " AND " + st.session_state.scene3.background3
        st.session_state.scene3.background3 = structured_model2.invoke(st.session_state.scene3.background3).background
        
        st.session_state.scene3.visual_description4 = st.session_state.scene3.visual_description4 + " AND " + st.session_state.scene3.background4
        st.session_state.scene3.background4 = structured_model2.invoke(st.session_state.scene3.background4).background
        
        st.session_state.scene3.visual_description5 = st.session_state.scene3.visual_description5 + " AND " + st.session_state.scene3.background5
        st.session_state.scene3.background5 = structured_model2.invoke(st.session_state.scene3.background5).background

        generatedscript=[
        st.session_state.scene1, st.session_state.scene2, st.session_state.scene3
            ]  
    return generatedscript
def calll():  
    if st.session_state.duretion == "5 minutes":
        
        st.session_state.sceness = [
            st.session_state.scenes.scene1,
            st.session_state.scenes.scene2,
            st.session_state.scenes.scene3,
            st.session_state.scenes.scene4,
            st.session_state.scenes.scene5,
            st.session_state.scenes.scene6,
            st.session_state.scenes.scene7,
            st.session_state.scenes.scene8
        ]
        
    elif st.session_state.duretion == "2 minutes":
        st.session_state.sceness = [
            st.session_state.scenes.scene1,
            st.session_state.scenes.scene2,
            st.session_state.scenes.scene3
        ]
    else:  # For longer durations
        st.session_state.sceness = [
            st.session_state.scenes.scene1,
            st.session_state.scenes.scene2,
            st.session_state.scenes.scene3,
            st.session_state.scenes.scene4,
            st.session_state.scenes.scene5
        ]
def narrative(prev=None,shot=None):
    
    abc=model1.invoke(f"""You will be given a sequence of sentences. Craft them into a coherent and immersive scene, focusing on the immediate sensory details and emotional atmosphere. Maintain the original order of the sentences. Aim for a scene description of **130 words**, without adding any new elements or information. 1) {shot.narrative1} 2) {shot.narrative2} 3) {shot.narrative3} 4) {shot.narrative4} 5) {shot.narrative5}""")
    while abc.usage_metadata["output_tokens"]<140 or abc.usage_metadata["output_tokens"]>160:
        # print(abc.usage_metadata["output_tokens"])
        # print(abc.content)
        print("\n\n")
        time.sleep(5)
        abc=model1.invoke(f"""You will be given a sequence of sentences. Craft them into a coherent and immersive scene, focusing on the immediate sensory details and emotional atmosphere. Maintain the original order of the sentences. Aim for a scene description of **130 words**, without adding any new elements or information. 1) {shot.narrative1} 2) {shot.narrative2} 3) {shot.narrative3} 4) {shot.narrative4} 5) {shot.narrative5}""")
    return  abc.content

def print_scene(scene,shots=None,narr=None,):
    prompt = shotprompt(scene.Characters,scene.summary_and_progression,scene.purpose_and_conflict,scene.CharacterDevelopment,scene.SettingElements,scene.narrativeVoice,shots)
    result = structured_model1.invoke(prompt)
    nar=narrative(narr,result)
    return result,nar


def shotprompt(characters, summary_and_progression, purpose_and_conflict, CharacterDevelopment, SettingElements, narrativeVoice, prevscenesummary=None):
    return f"""
    shots generated on previous scene **refer these to generate shots for next scene**:-
    : {prevscenesummary}
    
    **current Scene Description which you have to generate** :-
    
    Characters in this scene:
    - {characters}
    
    Summary and Progression:
    {summary_and_progression}
    
    Purpose and Conflict:
    {purpose_and_conflict}
    
    Character Development:
    {CharacterDevelopment}
    
    Setting Elements:
    {SettingElements}
    
    Narrative Voice:
    {narrativeVoice}
    
    """
    
if __name__ == "__main__":
    main()


    
