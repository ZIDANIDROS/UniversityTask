package com.example.mymusicplayer;

import java.io.IOException;
import java.nio.file.*;
import java.util.ArrayList;
import java.util.List;

public class MusicLoader {
    public static List<String> loadMusicFromDirectory(String directoryPath) {
        List<String> playlist = new ArrayList<>();
        try {
            Path directory = Paths.get(directoryPath);
            Path musicDirectory = directory.resolve("../music");
            DirectoryStream<Path> directoryStream = Files.newDirectoryStream(musicDirectory, "*.mp3");
            for (Path path : directoryStream) {
                playlist.add("music/" + path.getFileName());            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return playlist;
    }
}
