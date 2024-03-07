package com.example.mymusicplayer;

import javafx.scene.media.Media;
import javafx.scene.media.MediaPlayer;

import java.io.File;
import java.util.List;

public abstract class AbstractMusicPlayer implements MusicControl {
    protected Media media;
    protected MediaPlayer mediaPlayer;
    protected String currentSong = "";
    protected List<String> playlist;
    protected int currentSongIndex = 0;

    public abstract void initialize();

    protected void playCurrentSong() {
        String currentSongPath = playlist.get(currentSongIndex);
        media = new Media(new File(currentSongPath).toURI().toString());
        mediaPlayer = new MediaPlayer(media);

        mediaPlayer.setOnReady(() -> {
            setStatusLabel("Playing: " + currentSongPath);
            mediaPlayer.play();
            currentSong = currentSongPath;
        });
    }

    @Override
    public void playMusic() {
        if (mediaPlayer != null) {
            if (mediaPlayer.getStatus() == MediaPlayer.Status.PAUSED) {
                mediaPlayer.play();
                setStatusLabel("Playing: " + currentSong);
            } else if (mediaPlayer.getStatus() == MediaPlayer.Status.PLAYING) {
                setStatusLabel("Already playing: " + currentSong);
            } else {
                mediaPlayer.play();
                setStatusLabel("Playing: " + currentSong);
            }
        } else {
            playCurrentSong();
        }
    }

    @Override
    public void pauseMusic() {
        if (mediaPlayer != null && mediaPlayer.getStatus() == MediaPlayer.Status.PLAYING) {
            mediaPlayer.pause();
            setStatusLabel("Paused");
        }
    }

    @Override
    public void stopMusic() {
        if (mediaPlayer != null) {
            mediaPlayer.stop();
            setStatusLabel("Stopped");
        }
    }

    @Override
    public void nextMusic() {
        if (mediaPlayer != null && !playlist.isEmpty()) {
            mediaPlayer.stop();
            currentSongIndex = (currentSongIndex + 1) % playlist.size();
            playCurrentSong();
        }
    }

    @Override
    public void previousMusic() {
        if (mediaPlayer != null) {
            mediaPlayer.stop();
            currentSongIndex = (currentSongIndex - 1 + playlist.size()) % playlist.size();
            playCurrentSong();
        }
    }

    public void setVolume(double volume) {
        if (mediaPlayer != null) {
            mediaPlayer.setVolume(volume);
        }
    }



    protected abstract void setStatusLabel(String s);
}
