package com.example.mymusicplayer;

import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.Slider;
import javafx.scene.media.Media;
import javafx.scene.media.MediaPlayer;

import java.io.File;
import java.util.List;


public class MusicPlayerController extends AbstractMusicPlayer{
    @FXML
    private Label statusLabel;
    private Media media;
    private MediaPlayer mediaPlayer;
    private String currentSong = "";

    private int currentSongIndex = 0;
    private List<String> playlist;

    public void initialize() {
        playlist = MusicLoader.loadMusicFromDirectory("music");
        if (!playlist.isEmpty()) {
            playCurrentSong();
        } else {
            setStatusLabel("No music found!");
        }
    }

    @FXML
    private Slider volumeSlider;



    public void playMusic() {
        if (mediaPlayer != null) {
            if (mediaPlayer.getStatus() == MediaPlayer.Status.PAUSED) {
                mediaPlayer.play();
                setStatusLabel(currentSong);
            } else if (mediaPlayer.getStatus() == MediaPlayer.Status.PLAYING) {
                setStatusLabel("Already playing: " + currentSong);
            } else {
                mediaPlayer.play();
                setStatusLabel(currentSong);
            }
        } else {
            File audioFile = new File("music/ORQUESTRA MALDITA (BRAZILIAN PHONK).mp3");
            if (audioFile.exists()) {
                media = new Media(audioFile.toURI().toString());
                mediaPlayer = new MediaPlayer(media);

                mediaPlayer.setOnReady(() -> {
                    setStatusLabel(audioFile.getName());
                    mediaPlayer.play();
                    currentSong = audioFile.getName();
                });
            } else {
                setStatusLabel("File not found!");
            }
        }
    }


    public void pauseMusic() {
        if (mediaPlayer != null && mediaPlayer.getStatus() == MediaPlayer.Status.PLAYING) {
            mediaPlayer.pause();
            setStatusLabel("Paused");
        }
    }

    public void stopMusic() {
        if (mediaPlayer != null) {
            mediaPlayer.stop();
            statusLabel.setText("Stopped");
        }
    }

    protected void playCurrentSong() {
        String currentSongPath = playlist.get(currentSongIndex);
        File songFile = new File(currentSongPath);
        String currentSongName = songFile.getName();

        media = new Media(songFile.toURI().toString());
        mediaPlayer = new MediaPlayer(media);

        mediaPlayer.setOnReady(() -> {
            setStatusLabel(currentSongName);
            mediaPlayer.play();
            currentSong = currentSongPath;
        });
    }


    public void nextMusic() {
        if (mediaPlayer != null && !playlist.isEmpty()) {
            mediaPlayer.stop();
            currentSongIndex = (currentSongIndex + 1) % playlist.size();
            playCurrentSong();
        }
    }


    public void previousMusic() {
        if (mediaPlayer != null) {
            mediaPlayer.stop();
            currentSongIndex = (currentSongIndex - 1 + playlist.size()) % playlist.size();
            playCurrentSong();
        }
    }

    @Override



    public void setVolume(double volume) {
        if (mediaPlayer != null) {
            mediaPlayer.setVolume(volume);
        }
    }


    @Override
    protected void setStatusLabel(String s) {
        if (statusLabel != null) {
            statusLabel.setText(s);
        }
    }
}
