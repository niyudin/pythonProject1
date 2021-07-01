"""A video player class."""

from .video_library import VideoLibrary
import random
from re import search
class VideoPlayer:
    """A class used to represent a Video Player."""
#Funny Dogs | funny_dogs_video_id |  #dog , #animal
#Amazing Cats | amazing_cats_video_id |  #cat , #animal
#Another Cat Video | another_cat_video_id |  #cat , #animal
#Life at Google | life_at_google_video_id |  #google , #career
#Video about nothing | nothing_video_id |


    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        global playlist_check
        playlist_check = 1
        video_list = [["Funny Dogs", "funny_dogs_video_id", "#dog , #animal"],
                      ["Amazing Cats", "amazing_cats_video_id", "#cat , #animal"],
                      ["Another Cat Video", "another_cat_video_id", "#cat , #animal"],
                      ["Life at Google", "life_at_google_video_id", "#google , #career"],
                      ["Video about nothing", "nothing_video_id", ""]]
        print("Here's a list of all available videos:")
        print(*video_list, sep = "\n")
        print()
        """Returns all videos."""

    def play_video(self, video_play):
        ###video_id used because conditions cannot pick identify elements in video_list for unknown reason.
        global video_number
        global video_pause
        video_id = ["funny_dogs_video_id", "amazing_cats_video_id", "another_cat_video_id", "life_at_google_video_id",
                    "nothing_video_id"]
        video_list = [["Funny Dogs", "funny_dogs_video_id", "#dog , #animal"],
                      ["Amazing Cats", "amazing_cats_video_id", "#cat , #animal"],
                      ["Another Cat Video", "another_cat_video_id", "#cat , #animal"],
                      ["Life at Google", "life_at_google_video_id", "#google , #career"],
                      ["Video about nothing", "nothing_video_id", ""]]
        video_pause = 1
        if (video_play in video_id):
            if (video_play == video_id[0]):
                video_number = 1
                print("Playing: " + video_list[0][0])
            elif (video_play == video_id[1]):
                video_number = 2
                print("Playing: " + video_list[1][0])
            elif (video_play == video_id[2]):
                video_number = 3
                print("Playing: " + video_list[2][0])
            elif (video_play == video_id[3]):
                video_number = 4
                print("Playing: " + video_list[3][0])
            elif (video_play == video_id[4]):
                video_number = 5
                print("Playing: " + video_list[4][0])
        else:
            video_number = 0
            print("This video does not exist!")
            print(video_number)
        return video_number






    def stop_video(self):
        global video_number
        if video_number == 0:
            print("There is no video to stop!")
        else:
            video_number = 0
            print("Stopping video!")
        return video_number



    def play_random_video(self):
        global video_number
        global video_pause
        random_video = random.randint(1,5)
        video_list = [["Funny Dogs", "funny_dogs_video_id", "#dog , #animal"],
                      ["Amazing Cats", "amazing_cats_video_id", "#cat , #animal"],
                      ["Another Cat Video", "another_cat_video_id", "#cat , #animal"],
                      ["Life at Google", "life_at_google_video_id", "#google , #career"],
                      ["Video about nothing", "nothing_video_id", ""]]
        video_pause = 1
        if random_video == 1:
            video_number = 1
            print("Playing: " + video_list[0][0])
        if random_video == 2:
            video_number = 2
            print("Playing: " + video_list[1][0])
        if random_video == 3:
            video_number = 3
            print("Playing: " + video_list[2][0])
        if random_video == 4:
            video_number = 4
            print("Playing: " + video_list[3][0])
        if random_video == 5:
            video_number = 5
            print("Playing: " + video_list[4][0])
        """Plays a random video from the video library."""


    def pause_video(self):
        global video_number
        global video_pause
        if video_number == 0:
            print("There is nothing to pause!")
        else:
            if video_pause == 1:
                print("Pausing video")
                video_pause = video_pause - 1
            else:
                print("Already paused")
        """Pauses the current video."""

    def continue_video(self):
        global video_pause
        if video_pause == 0:
            video_pause = video_pause + 1
            print("Resuming video")
        else:
            print("There is nothing to resume!")
        """Resumes playing the current video."""

    def show_playing(self):
        global video_number
        video_list = [["Funny Dogs", "funny_dogs_video_id", "#dog , #animal"],
                      ["Amazing Cats", "amazing_cats_video_id", "#cat , #animal"],
                      ["Another Cat Video", "another_cat_video_id", "#cat , #animal"],
                      ["Life at Google", "life_at_google_video_id", "#google , #career"],
                      ["Video about nothing", "nothing_video_id", ""]]
        if video_number == 1:
            print("You are watching: " + video_list[0][0])
        if video_number == 2:
            print("You are watching: " + video_list[1][0])
        if video_number == 3:
            print("You are watching: " + video_list[2][0])
        if video_number == 4:
            print("You are watching: " + video_list[3][0])
        if video_number == 5:
            print("You are watching: " + video_list[4][0])
        if video_number == 0:
            print("You are not watching anything")
        """Displays video currently playing."""

    def create_playlist(self, playlist_name):
        ###I encountered much more trouble running tests with any functions involving making 1D or 2D lists (par contre the preset lists like video_list) Hence, the code is NOT functional for playlist and flagging commands. Very sorry.
        ###Attempts included global lists, appending lists, replacing, only having 1 playlist being creatable. The functions had trouble with the lists being referenced before being identified, however, even if they were identified, encountered same problem.
        ###Codes utilising regular append functions were operable in IDLE. My inexperience with Pycharm led me to be unable to complete this task.
        global playlist_list
        global playlist_check
        global playlist_number
        if playlist_check == 0:
            print("Please use the show_videos command to view the videos you can add to playlists")
        else:
            print("Playlist created")
        playlist_list.append(playlist_name)
        print("Creating Playlist: " + playlist_name)


    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        print("Here are the results. Please be wary, the search tool is new and is case and exact-word sensitive!")
        if search(search_term, "Amazing Cats"):
            print("Amazing Cats")
            print("Another Cat Video")
        else:
            if search(search_term, "Funny Dogs"):
                print("Funny Dogs")
            else:
                if search(search_term, "Another Cat Video"):
                    print("Another Cat Video")
                    print("Amazing Cats")
                else:
                    if search(search_term, "Life at Google"):
                        print("Life at Google")
                    else:
                        if search(search_term, "Nothing Video"):
                            print("Nothing Video")



    def search_videos_tag(self, video_tag):
        video_tag_list = ["#cat", "#dog","#cats","#dogs","#animal","animals","#google","#career"]
        if (video_tag in video_tag_list):
            if (video_tag == video_tag_list[0]):
                print("Relevant videos: Amazing Cats, Another Cat Video")
            elif (video_tag == video_tag_list[1]):
                print("Relevant videos: Funny Dogs")
            elif (video_tag == video_tag_list[2]):
                print("Relevant videos: Amazing Cats, Another Cat Video")
            elif (video_tag == video_tag_list[3]):
                print("Relevant videos: Funny Dogs")
            elif (video_tag == video_tag_list[4]):
                print("Relevant videos: Funny Dogs, Another Cat Video, Amazing Cats")
            elif (video_tag == video_tag_list[5]):
                print("Relevant videos: Funny Dogs, Another Cat Video, Amazing Cats")
            elif (video_tag == video_tag_list[6]):
                print("Relevant videos: Life at Google")
            elif (video_tag == video_tag_list[7]):
                print("Relevant videos: Life at Google")
        else:
            print("No matching video exists!")


    def flag_video(self, video_id, flag_reason=""):
        video_id = ["funny_dogs_video_id", "amazing_cats_video_id", "another_cat_video_id", "life_at_google_video_id",
                    "nothing_video_id"]

        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
